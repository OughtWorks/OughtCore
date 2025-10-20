#!/usr/bin/env python3
"""
Harvest NOTE / TODO / REFLECTION blocks from SpecPrime-style chatlogs.

Chatlogs live under: Playground/chatlogs/YYYY-MM/
Each chat file is named after its session_id: sp-xxxxxxxx.md

Usage:
    python tools/harvest_chat.py --month 2025-10
"""

import argparse, os, re, uuid, datetime, pathlib, json
from textwrap import dedent

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
PLAYGROUND = os.path.expanduser("~/Projects/Playground")
CHATROOT   = os.path.join(PLAYGROUND, "chatlogs")
NOTES_DIR  = os.path.join(PLAYGROUND, "notes")
TODOS_OPEN = os.path.join(PLAYGROUND, "todos", "open")
TODOS_DONE = os.path.join(PLAYGROUND, "todos", "done")
META_DIR   = os.path.join(PLAYGROUND, "meta", "indices")

# ---------------------------------------------------------------------------
# Regex patterns
# ---------------------------------------------------------------------------

# Matches a capture block header and body per SpecPrime contract
BLOCK_RE = re.compile(
    r"(?ms)^##\s*(NOTE|TODO|REFLECTION|TODO-STATUS|NOTE-UPDATE)\s*—?\s*(.*?)\n"
    r"(?:UUID:\s*(?P<uuid>.+?)\n"
    r"PROJECT:\s*(?P<project>.+?)\n"
    r"(?:TAGS:\s*\[(?P<tags>.*?)\]\n)?"
    r"CREATED_AT:\s*(?P<created>.+?)\n"
    r"(?:(?:PRIORITY|STATUS|DUE|REF_UUID).*?\n)*?)"
    r"BODY:\n(?P<body>.*?)(?=^##\s|\Z)"
)

STATUS_RE = re.compile(r"STATUS:\s*(\w+)")
REF_RE    = re.compile(r"REF_UUID:\s*(\S+)")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def ensure_dirs():
    for path in [NOTES_DIR, TODOS_OPEN, TODOS_DONE, META_DIR]:
        os.makedirs(path, exist_ok=True)

def clean_slug(title: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", title.strip().lower())[:60].strip("-")
    return slug or "untitled"

def write_markdown(kind, uuid_, project, tags, created, title, body, srcfile):
    """Write a normalized markdown file with YAML front-matter."""
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    tags_list = [t.strip() for t in tags.split(",")] if tags else []
    meta = dedent(f"""\
        ---
        uuid: {uuid_}
        kind: {kind.lower()}
        project: {project}
        tags: {tags_list}
        created_at: {created.strip()}
        harvested_at: {ts}
        source_chat: {os.path.basename(srcfile)}
        ---
    """)
    content = meta + "\n" + body.strip() + "\n"

    slug = clean_slug(title)
    outdir = NOTES_DIR
    if kind.startswith("TODO"):
        # decide done/open
        status_match = STATUS_RE.search(body)
        status = status_match.group(1).lower() if status_match else "open"
        outdir = TODOS_DONE if status == "done" or kind == "TODO-STATUS" else TODOS_OPEN
    outfile = os.path.join(outdir, f"{uuid_}--{slug}.md")
    with open(outfile, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ {kind:<12} {outfile}")
    return {
        "uuid": uuid_,
        "kind": kind,
        "title": title,
        "project": project,
        "tags": tags_list,
        "created_at": created.strip(),
        "path": outfile,
        "source_chat": os.path.basename(srcfile)
    }

# ---------------------------------------------------------------------------
# Core harvesting logic
# ---------------------------------------------------------------------------

def harvest(month: str):
    """Harvest all chat files under chatlogs/YYYY-MM/."""
    ensure_dirs()
    chatdir = os.path.join(CHATROOT, month)
    if not os.path.isdir(chatdir):
        print(f"❌ No chatlogs found for {month} in {chatdir}")
        return

    files = sorted(pathlib.Path(chatdir).glob("sp-*.md"))
    all_index = []
    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        matches = list(BLOCK_RE.finditer(text))
        if not matches:
            print(f"⚪  No harvestable blocks in {path.name}")
            continue
        for m in matches:
            block = write_markdown(
                kind     = m.group(1),
                uuid_    = m.group("uuid").strip(),
                project  = m.group("project").strip(),
                tags     = m.group("tags") or "",
                created  = m.group("created"),
                title    = m.group(2).strip(),
                body     = m.group("body"),
                srcfile  = str(path)
            )
            all_index.append(block)

    # write/update month index
    if all_index:
        index_file = os.path.join(META_DIR, f"indices-{month}.json")
        existing = []
        if os.path.exists(index_file):
            try:
                existing = json.loads(open(index_file).read())
            except Exception:
                pass
        existing.extend(all_index)
        with open(index_file, "w", encoding="utf-8") as f:
            json.dump(existing, f, indent=2)
        print(f"📚  Index updated: {index_file}")
    print(f"🎯 Harvest complete — {len(all_index)} blocks written.")

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--month", required=True, help="Month folder (YYYY-MM)")
    args = ap.parse_args()
    harvest(args.month)
