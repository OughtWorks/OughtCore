#!/usr/bin/env python3
"""
Harvest NOTE / TODO / REFLECTION style blocks from chat transcripts.

The parser expects SpecPrime capture-contract headings:
	## NOTE — <title>
	## TODO — <title>
	## REFLECTION — <title>
	## TODO-STATUS — <title>
	## NOTE-UPDATE — <title>

Each block must include header fields (UUID, PROJECT, TAGS, CREATED_AT, ...)
followed by a BODY stanza. Harvested artifacts are written into the
Playground workspace and a monthly JSON index.
"""

import argparse
import datetime
import json
import os
import pathlib
import re
import shutil
from dataclasses import dataclass
from textwrap import dedent
from typing import Dict, Iterable, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
PLAYGROUND = os.path.expanduser("~/Projects/Playground")
CHATROOT = os.path.join(PLAYGROUND, "chatlogs")
NOTES_DIR = os.path.join(PLAYGROUND, "notes")
TODOS_OPEN = os.path.join(PLAYGROUND, "todos", "open")
TODOS_DONE = os.path.join(PLAYGROUND, "todos", "done")
META_DIR = os.path.join(PLAYGROUND, "meta", "indices")
MALFORMED_DIR = os.path.join(PLAYGROUND, "malformed")

# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

HEADER_RE = re.compile(
	r"(?m)^##\s*(NOTE|TODO|REFLECTION|TODO-STATUS|NOTE-UPDATE)\s*(?:—|-)?\s*(.*)$"
)
SETEXT_HEADER_RE = re.compile(
	r"(?m)^(NOTE|TODO|REFLECTION|TODO-STATUS|NOTE-UPDATE)\s*(?:—|-)\s*(.*?)\n[-=]{3,}\s*$"
)
FIELD_RE = re.compile(r"^([A-Z][A-Z0-9_-]*):\s*(.*)$")

REQUIRED_FIELDS = ("UUID", "PROJECT", "CREATED_AT")


@dataclass
class HarvestBlock:
	kind: str
	title: str
	fields: Dict[str, str]
	body: str
	raw: str


def ensure_dirs() -> None:
	"""Make sure the core directories exist."""
	for path in [NOTES_DIR, TODOS_OPEN, TODOS_DONE, META_DIR, MALFORMED_DIR]:
		os.makedirs(path, exist_ok=True)


def clean_slug(title: str) -> str:
	slug = re.sub(r"[^a-zA-Z0-9]+", "-", title.strip().lower())[:60].strip("-")
	return slug or "untitled"


def parse_tags(raw: Optional[str]) -> List[str]:
	if not raw:
		return []
	text = raw.strip()
	if text.startswith("[") and text.endswith("]"):
		text = text[1:-1]
	if not text.strip():
		return []
	return [t.strip().strip("\"'") for t in text.split(",") if t.strip()]


def normalize_fields(lines: Iterable[str]) -> Tuple[Dict[str, str], str]:
	fields: Dict[str, str] = {}
	body_lines: List[str] = []
	in_body = False
	current_key: Optional[str] = None

	for raw_line in lines:
		line = raw_line.rstrip("\n")
		stripped = line.strip()
		if not in_body:
			if not stripped:
				continue
			if stripped.upper() == "BODY:":
				in_body = True
				current_key = None
				continue
			match = FIELD_RE.match(stripped)
			if match:
				current_key = match.group(1).upper()
				fields[current_key] = match.group(2).strip()
			else:
				# Treat continuation lines as part of the previous field value.
				if current_key:
					fields[current_key] = (
						fields[current_key] + "\n" + stripped
					)
		else:
			body_lines.append(line.rstrip())
	body = "\n".join(body_lines).rstrip()
	return fields, body


def find_headers(text: str) -> List[Tuple[int, int, str, str]]:
	headers: List[Tuple[int, int, str, str]] = []
	for match in HEADER_RE.finditer(text):
		start = match.start()
		content_start = match.end()
		if content_start < len(text) and text[content_start] == "\n":
			content_start += 1
		headers.append(
			(start, content_start, match.group(1).upper(), match.group(2).strip())
		)
	for match in SETEXT_HEADER_RE.finditer(text):
		start = match.start()
		content_start = match.end()
		headers.append(
			(start, content_start, match.group(1).upper(), match.group(2).strip())
		)
	headers.sort(key=lambda item: item[0])
	return headers


def iter_blocks(text: str) -> Iterable[HarvestBlock]:
	headers = find_headers(text)
	for idx, (start, content_start, kind, title) in enumerate(headers):
		end = headers[idx + 1][0] if idx + 1 < len(headers) else len(text)
		content = text[content_start:end].lstrip("\n")
		fields, body = normalize_fields(content.splitlines())
		yield HarvestBlock(
			kind=kind,
			title=title,
			fields={k.upper(): v for k, v in fields.items()},
			body=body,
			raw=content,
		)


def save_malformed(block: HarvestBlock, path: pathlib.Path, missing) -> None:
	os.makedirs(MALFORMED_DIR, exist_ok=True)
	fname = f"{block.fields.get('UUID', 'unknown')}--malformed.md"
	fpath = os.path.join(MALFORMED_DIR, fname)
	if isinstance(missing, (list, tuple, set)):
		missing_str = ", ".join(str(item) for item in missing)
	else:
		missing_str = str(missing)
	meta = [
		"---",
		f"harvest_warning: {missing_str}",
		f"source_chat: {path.name}",
		f"detected_kind: {block.kind}",
		f"detected_title: {block.title}",
		"---",
		"",
	]
	with open(fpath, "w", encoding="utf-8") as handle:
		handle.write("\n".join(meta))
		handle.write(block.raw)
	print(f"🗑️  Malformed {block.kind} saved for review: {fpath}")


# ---------------------------------------------------------------------------
# Writing helpers
# ---------------------------------------------------------------------------

def build_front_matter(
	block: HarvestBlock,
	tags: List[str],
	uuid_value: str,
	project: str,
	created_at: str,
	session_id: str,
	seq: str,
	source_chat: str,
) -> str:
	ts = datetime.datetime.now().isoformat(timespec="seconds")
	base_meta: Dict[str, object] = {
		"uuid": uuid_value,
		"kind": block.kind.lower(),
		"title": block.title or block.fields.get("TITLE", ""),
		"project": project,
		"tags": tags,
		"created_at": created_at.strip(),
		"harvested_at": ts,
		"source_chat": source_chat,
		"session_id": session_id,
		"sequence": seq,
	}

	for optional in (
		"OWNER",
		"PHASE",
		"INTENT",
		"PRIORITY",
		"STATUS",
		"DUE",
		"REF_UUID",
	):
		value = block.fields.get(optional)
		if value:
			base_meta[optional.lower()] = value

	lines = ["---"]
	for key, value in base_meta.items():
		if isinstance(value, list):
			lines.append(f"{key}: {value}")
		else:
			lines.append(f"{key}: {value}")
	lines.append("---")
	return "\n".join(lines)


def write_block_file(
	block: HarvestBlock,
	outdir: str,
	uuid_value: str,
	title: str,
	project: str,
	tags: List[str],
	created_at: str,
	srcfile: str,
) -> str:
	os.makedirs(outdir, exist_ok=True)
	slug = clean_slug(title or block.fields.get("TITLE", "") or uuid_value)
	outfile = os.path.join(outdir, f"{uuid_value}--{slug}.md")

	session_id, seq = split_uuid(uuid_value)
	front_matter = build_front_matter(
		block,
		tags,
		uuid_value,
		project,
		created_at,
		session_id,
		seq,
		os.path.basename(srcfile),
	)
	body = block.body.strip("\n")
	content = front_matter + "\n\n" + (body + "\n" if body else "")
	with open(outfile, "w", encoding="utf-8") as handle:
		handle.write(content)
	return outfile


def split_uuid(uuid_value: str) -> Tuple[str, str]:
	if "#" in uuid_value:
		session_id, seq = uuid_value.split("#", 1)
		return session_id, seq
	return uuid_value, ""


def find_todo_file(ref_uuid: str) -> Optional[str]:
	pattern = f"{ref_uuid}--*.md"
	for root in (TODOS_OPEN, TODOS_DONE):
		for candidate in pathlib.Path(root).glob(pattern):
			return str(candidate)
	return None


def apply_todo_status(block: HarvestBlock) -> Optional[str]:
	ref_uuid = block.fields.get("REF_UUID")
	if not ref_uuid:
		print("⚠️  TODO-STATUS missing REF_UUID; block skipped.")
		return None
	target = find_todo_file(ref_uuid)
	if not target:
		print(f"⚠️  TODO-STATUS could not find TODO {ref_uuid}; block skipped.")
		return None
	status = (block.fields.get("STATUS") or "").strip().lower()
	dest_path = target
	if status == "done" and target.startswith(TODOS_OPEN):
		os.makedirs(TODOS_DONE, exist_ok=True)
		dest_path = os.path.join(TODOS_DONE, os.path.basename(target))
		shutil.move(target, dest_path)
	update = "\n".join(
		[
			"",
			f"<!-- TODO-STATUS update from {block.fields.get('UUID', 'unknown')} -->",
			block.body.strip(),
			"",
		]
	)
	with open(dest_path, "a", encoding="utf-8") as handle:
		handle.write(update)
	print(f"✅ TODO-STATUS {ref_uuid} → {status or 'updated'} ({dest_path})")
	return dest_path


# ---------------------------------------------------------------------------
# Harvest execution
# ---------------------------------------------------------------------------

def harvest_file(path: pathlib.Path) -> List[Dict[str, object]]:
	text = path.read_text(encoding="utf-8", errors="ignore")
	harvested: List[Dict[str, object]] = []

	for block in iter_blocks(text):
		missing = [key for key in REQUIRED_FIELDS if key not in block.fields]
		if missing:
			save_malformed(block, path, missing)
			continue
		if not block.body:
			print(f"⚪  Skipping {block.kind} — empty body in {path.name}")
			save_malformed(block, path, "empty body")
			continue

		uuid_value = block.fields["UUID"].strip()
		project = block.fields["PROJECT"].strip()
		created_at = block.fields["CREATED_AT"].strip()
		tags = parse_tags(block.fields.get("TAGS"))
		title = block.title or block.fields.get("TITLE", "").strip()

		if block.kind == "TODO-STATUS":
			apply_todo_status(block)
			continue
		if block.kind == "NOTE-UPDATE":
			print("⚪  NOTE-UPDATE handling not implemented yet; skipping.")
			continue

		outdir = NOTES_DIR
		status = (block.fields.get("STATUS") or "").strip().lower()
		if block.kind == "TODO":
			outdir = TODOS_DONE if status == "done" else TODOS_OPEN
		elif block.kind == "REFLECTION":
			outdir = NOTES_DIR

		outfile = write_block_file(
			block,
			outdir,
			uuid_value,
			title,
			project,
			tags,
			created_at,
			str(path),
		)
		print(f"✅ {block.kind:<12} {outfile}")

		session_id, seq = split_uuid(uuid_value)
		harvested.append(
			{
				"uuid": uuid_value,
				"kind": block.kind,
				"title": title,
				"project": project,
				"tags": tags,
				"created_at": created_at,
				"path": outfile,
				"source_chat": path.name,
				"session_id": session_id,
				"sequence": seq,
			}
		)
	return harvested


def write_index(month: str, new_entries: List[Dict[str, object]]) -> None:
	if not new_entries:
		return
	index_file = os.path.join(META_DIR, f"indices-{month}.json")
	existing: Dict[str, Dict[str, object]] = {}
	if os.path.exists(index_file):
		try:
			with open(index_file, "r", encoding="utf-8") as handle:
				data = json.load(handle)
				existing = {item["uuid"]: item for item in data if "uuid" in item}
		except Exception:
			existing = {}
	for entry in new_entries:
		existing[entry["uuid"]] = entry
	entries = list(existing.values())
	entries.sort(key=lambda item: (item.get("created_at", ""), item.get("uuid", "")))
	with open(index_file, "w", encoding="utf-8") as handle:
		json.dump(entries, handle, indent=2)
	print(f"📚  Index updated: {index_file}")


def harvest(month: str) -> None:
	ensure_dirs()
	chatdir = pathlib.Path(CHATROOT) / month
	if not chatdir.is_dir():
		print(f"❌ No chatlogs found for {month} in {chatdir}")
		return

	files = sorted(chatdir.glob("sp-*.md"))
	if not files:
		print(f"⚪  No chatlogs matched sp-*.md in {chatdir}")
		return

	harvested_entries: List[Dict[str, object]] = []
	for path in files:
		results = harvest_file(path)
		if not results:
			print(f"⚪  No harvestable blocks in {path.name}")
		harvested_entries.extend(results)

	write_index(month, harvested_entries)
	print(f"🎯 Harvest complete — {len(harvested_entries)} blocks written.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
	parser = argparse.ArgumentParser()
	parser.add_argument("--month", required=True, help="Month folder (YYYY-MM)")
	args = parser.parse_args()
	harvest(args.month)


if __name__ == "__main__":
	main()
