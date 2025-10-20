That layout gives you a really clean, human-and-machine friendly shape:

```
Playground/chatlogs/
└── 2025-10/
    ├── sp-a7c9f2bd.md
    ├── sp-e12f0034.md
    └── sp-77ac91e0.md
```

Each file is the markdown transcript for one session.
Below is a full `tools/harvest_chat.py` that assumes that structure and the **SpecPrime Capture Contract** grammar you just locked in.

---

### 🧩  `tools/harvest_chat.py`

```python
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
```

---

### 🧪  How to test

1. Save the script as `OughtCore/tools/harvest_chat.py`.
2. Make it executable:

   ```bash
   chmod +x OughtCore/tools/harvest_chat.py
   ```
3. From your repo root:

   ```bash
   python tools/harvest_chat.py --month 2025-10
   ```

You’ll get output like:

```
✅ NOTE         /Playground/notes/2025-10/sp-a7c9f2bd#001--filetree-target-anatomy.md
✅ TODO         /Playground/todos/open/sp-a7c9f2bd#002--implement-harvest-target.md
⚪  No harvestable blocks in sp-77ac91e0.md
📚  Index updated: Playground/meta/indices/indices-2025-10.json
🎯 Harvest complete — 2 blocks written.
```

---

### 🧠  How it behaves

| Behavior                                                               | Result                                             |
| ---------------------------------------------------------------------- | -------------------------------------------------- |
| Reads each chat file in `chatlogs/YYYY-MM/` named after its session ID | Keeps your session → UUID chain intact             |
| Parses blocks using the SpecPrime grammar                              | Ignores other Markdown clutter                     |
| Writes normalized Markdown files with YAML front-matter                | Each note/todo is atomic                           |
| Determines open/done status from the block body                        | Routes correctly to `todos/open/` or `todos/done/` |
| Appends all block metadata to a monthly JSON index                     | Enables future search and dashboard queries        |

---

### 🪄  Next (optional niceties)

* Add a small validator that warns if any block is missing `UUID:` or `BODY:`.
* Insert `make harvest` in your Makefile:

```makefile
harvest:
	@python tools/harvest_chat.py --month $(shell date +%Y-%m)
```

Then you can just run:

```bash
make harvest
```

That’s the **working harvester** for your new chat-UUID system.


---

### 🗂️  Output map

Everything the harvester writes goes **inside your `~/Projects/Playground/` repo**, mirroring the structure you designed earlier.

```
Playground/
├── notes/                ← all NOTE and REFLECTION blocks
│   ├── 2025-10/          ← optional monthly subfolders (can be added later)
│   └── sp-a7c9f2bd#001--filetree-target-anatomy.md
├── todos/
│   ├── open/             ← active TODOs (STATUS=open)
│   │   └── sp-a7c9f2bd#002--implement-harvest-target.md
│   └── done/             ← completed TODOs or TODO-STATUS blocks
│       └── sp-a7c9f2bd#005--implement-harvest-target.md
├── meta/
│   └── indices/
│       └── indices-2025-10.json   ← monthly JSON index of all harvested blocks
└── chatlogs/
    └── 2025-10/
        ├── sp-a7c9f2bd.md         ← your original chat export (input)
        └── sp-77ac91e0.md
```

---

### 📦  File contents

**Each harvested file** (note/todo) contains YAML-style front-matter followed by the body pulled from the chat:

```markdown
---
uuid: sp-a7c9f2bd#002
kind: todo
project: OughtCore
tags: ['harvest','parser']
created_at: 2025-10-15
harvested_at: 2025-10-16T12:00:32
source_chat: sp-a7c9f2bd.md
---
- Write tools/harvest_chat.py to extract NOTE/TODO/REFLECTION.
- Save to Playground/notes and Playground/todos/open.
```

---

### 🧾  Index file

The monthly index (`meta/indices/indices-2025-10.json`) is a JSON list of all harvested blocks so other tools can query it:

```json
[
  {
    "uuid": "sp-a7c9f2bd#001",
    "kind": "NOTE",
    "title": "filetree target anatomy",
    "project": "OughtCore",
    "tags": ["makefile","filetree","tooling"],
    "created_at": "2025-10-15",
    "path": "/Users/you/Projects/Playground/notes/sp-a7c9f2bd#001--filetree-target-anatomy.md",
    "source_chat": "sp-a7c9f2bd.md"
  },
  {
    "uuid": "sp-a7c9f2bd#002",
    "kind": "TODO",
    "title": "implement harvest target",
    "project": "OughtCore",
    "tags": ["harvest","parser"],
    "created_at": "2025-10-15",
    "path": "/Users/you/Projects/Playground/todos/open/sp-a7c9f2bd#002--implement-harvest-target.md",
    "source_chat": "sp-a7c9f2bd.md"
  }
]
```

---

### 🧠  Quick mental model

| Source                           | Output                                                  | Rule                |
| -------------------------------- | ------------------------------------------------------- | ------------------- |
| `## NOTE` / `## REFLECTION`      | `Playground/notes/`                                     | always notes        |
| `## TODO` (`STATUS=open`)        | `Playground/todos/open/`                                | active tasks        |
| `## TODO-STATUS` (`STATUS=done`) | `Playground/todos/done/`                                | completed           |
| `## NOTE-UPDATE`                 | *append to existing note* (or later, `/notes/updates/`) | future improvement  |
| All blocks (any kind)            | `meta/indices/indices-YYYY-MM.json`                     | searchable metadata |

---

After you run:

```bash
python tools/harvest_chat.py --month 2025-10
```

you’ll open your `Playground/notes/` and `Playground/todos/open/` folders and literally see new `.md` files there — that’s your proof of life.
