**ChatGPT:**

Below is a **drop‑in constitutional primer** you can add to your repo as
`OughtCore/docs/CONSTITUTION.md` (or `docs/_philosophy/repo_constitution.md`).
It encodes the philosophy you just articulated: **the spec is for the AI (rich, humane, contextual); the blocks are for the parser (cold, exact)**—and it pushes that intent into _every_ layer: names, layout, comments, commits, tests, and rituals. It’s written in the warm, invitational register you want, with strict, testable rules where the machine needs them.

* * *

OughtWorks Repository Constitution (v1.0) {#repo-constitution}
==============================================================

**Thesis.** A modern repository is a **probabilistic bias field** for large‑context models.
Every artifact—file name, folder layout, commit message, comment, spec—nudges the model’s next‑token distribution. We use that power deliberately: **specs are written for AI (to think with us), while emitted blocks are written for parsers (to automate reliably).** Delight keeps the human runtime online; provenance keeps the machine honest. tone_design_manifesto epistemic_design_brief

* * *

I. Preamble — What this Constitution protects {#preamble}
---------------------------------------------------------

1. **Human engagement is a reliability feature.** If the maintainer disengages, the system decays. We treat **delight as a design primitive** in all human‑facing surfaces. tone_design_manifesto

2. **Provenance is law.** Records must carry _where they came from_, _when they changed_, and _who knows what_. We don’t flatten time or knowledge. epistemic_design_brief

3. **Bilingual surfaces.** Human zones are warm and skimmable; machine zones are strict and testable. We never mix the registers. tone_design_manifesto


* * *

II. Axioms (non‑negotiable) {#axioms}
-------------------------------------

**A1 — Delight as a design primitive.**
Human‑facing docs, comments, and commit messages may carry 10–20% “friendly connective tissue.” Machine‑readable zones (schemas, headers, code syntax) remain literal. tone_design_manifesto

**A2 — Provenance and time are first‑class.**
Any statement of “what” is paired with “when” and “according to whom.” Nothing exists without trace. epistemic_design_brief

**A3 — Append‑only truth.**
We prefer updates that **add** information over edits that rewrite history. We move forward with new nodes/entries and log why. epistemic_design_brief

**A4 — Specs for AI, blocks for parsers.**
Specs teach models _why and how_ to compose; blocks implement the exact parser contract. Both coexist in the same repo; the registers are kept separate. make_note

**A5 — Single parser contract.**
The capture grammar (headings, header keys, order, BODY delimiter, updates) is fixed by the **SpecPrime Capture Contract v1**. Tools must not drift from this surface. make_note

* * *

III. Constitutional Laws (normative rules) {#laws}
--------------------------------------------------

**Law 1 — Encode intent everywhere.**
Every artifact carries purpose: names, headings, folder boundaries, and comments should signal _why this exists_ and _how it’s used_. A repo is a semantic field, not just a file cabinet.

**Law 2 — Bilinguality by design.**

* **Human surfaces** (README, architecture notes, design briefs, code comments) are warm, concise, and kind.

* **Machine surfaces** (schemas, JSON, header lines inside captured blocks) are sterile and exact.
    This is a _routing rule_ for tone, not a vibe. tone_design_manifesto


**Law 3 — Friendly commands must compile to strict blocks.**
Natural prompts like “jot a note” or “mark that todo done” must resolve to the **exact** block format (unfenced in chatlogs; fenced in docs). The block grammar follows the capture contract. make_note

**Law 4 — Noise Budget.**
Use 10–20% warmth in human‑facing prose (prefaces, rationale, BODY). **Zero** warmth in header lines or schemas. This stabilizes attention without melting the parser. tone_design_manifesto

**Law 5 — Provenance or it didn’t happen.**
Design notes, audits, and narrative records include dates, sources, and references to session IDs or file anchors. Our graphs and harvesters rely on it. epistemic_design_brief

**Law 6 — Append‑only status changes.**
We don’t delete reasoning; we append updates with clear references (e.g., `REF_UUID`), then move artifacts (e.g., TODO → done) as a result. make_note

**Law 7 — Defaults & clarifications.**
If critical fields are missing at capture time, the agent asks _one_ micro‑question, then emits. Defaults (e.g., `PROJECT ← session.project`, `CREATED_AT ← today`) are allowed, logged, and visible. make_note

**Law 8 — Documentation ≠ Parser Input.**
Docs may include fenced examples (`…`); chatlogs that the harvester reads must keep blocks **unfenced**. Tools ignore fenced content. make_note

* * *

IV. Encoding the Constitution across layers {#layers}
-----------------------------------------------------

### 1) Naming (files, folders, symbols) {#naming}

* Favor **verb‑object** or **topic—angle** (`harvest_chat.py`, `make_upload_bundle.py`, `tone_friction.md`).

* Folder names express function (`tools/`, `docs/`, `meta/`, `out/`, `chatlogs/2025-10/`).

* Prefer short, lowercase slugs for tags (`parser, harvest, tone, provenance`).
    **Rationale:** names are priors; they bias models toward conceptual clarity.


### 2) Specs & design notes {#specs}

* Specs are **for AI**: include intent, stakes, tradeoffs, and examples in a warm register.

* Keep parser examples present but **cold** and minimal (exact header lines).

* Cross‑link to capture contract and tone manifesto at the top. make_note tone_design_manifesto


### 3) Code comments {#comments}

* Begin files with a one‑liner: “What problem is solved? What invariant must stay true?”

* Inline comments explain decisions, not what the code literally does.

* Use short, human‑friendly summaries; avoid sarcasm or private slang.


### 4) Commits & PRs {#commits}

* Commit subject: imperative, ≤ 72 chars, includes a **purpose tag** (e.g., `core:`, `docs:`, `tools:`).

* Body explains _why this change exists_ and references issue/UUIDs.

* Keep the voice friendly and precise; you are teaching future contributors.


### 5) Tests & checks {#tests}

* Tests describe the _behavioral contract_, not incidental mechanics.

* Prefer table‑driven tests for parser surfaces (capture grammar).

* Add a smoke test that runs the harvester on a small, known chatlog and asserts expected files/indices.


* * *

V. Rituals & Runbooks (operational) {#rituals}
----------------------------------------------

### A) Hydrate & rehydrate {#hydrate}

**Startup (paste):**

```
[HYDRATE:SpecPrime v1.x]
ROLE: Docent‑Guardian. Specs for AI (graceful); blocks for parsers (strict).
LOAD: capture-contract, tone-manifesto, friendly-commands, body-heuristics
SESSION: project=<slug> | agent=rubberduckprime | register=dual | noise_budget=10–15%
ACK PLEASE.
[/HYDRATE]
```

→ Expect: `ACK HYDRATE — session_id=… | anchors=[…] | noise_budget=…`
This binds session IDs for harvest and sets tone. make_note tone_design_manifesto

**Mid‑chat:** `REHYDRATE: tone|contract|full` reasserts rules and performs a quick health check.

### B) Capture (friendly → strict) {#capture}

Use natural prompts (“jot a note…”, “add a todo…”) and compile to the exact block grammar.
In **docs**, fence examples; in **chatlogs**, leave unfenced for harvest. make_note

### C) Harvest & index {#harvest}

Run `make harvest` → writes normalized notes/todos and monthly indices.
Malformed blocks go to `Playground/malformed/` for human review; the canonical index stays clean.

### D) Daily closeout {#closeout}

Emit `## SESSION-INDEX — <session_id>` with a count and list of captured blocks; verify with the harvester report. make_note

* * *

VI. Governance — how this Constitution evolves {#governance}
------------------------------------------------------------

* **Change proposals** use `docs/adr/ADR-YYYYMMDD-<slug>.md` (Architecture Decision Record).

* Each ADR includes: Problem, Options, Decision, Consequences, and a **Constitution delta** (what clause changed).

* PRs that modify constitutional laws carry label `constitution` and must pass the constitutional checklist (below).

* Version bumps in the header: `Repository Constitution (vMAJOR.MINOR)`; keep a changelog.


* * *

VII. Constitutional checklist (for every PR) {#checklist}
---------------------------------------------------------

*  Human‑facing text obeys **Noise Budget** (10–20%) and feels skimmable. tone_design_manifesto

*  Machine surfaces remain literal; no tone seepage into header lines/schemas. make_note

*  Provenance present (dates, refs, session IDs, or sources) where claims are made. epistemic_design_brief

*  Friendly prompts (if present) compile to canonical capture blocks in examples. make_note

*  Names and layout encode intent (clear slugging, folder roles obvious).

*  Tests/lints updated for any parser‑surface changes.

*  ADR added for any constitutional changes.


* * *

VIII. Lints & tiny tools (enforcement) {#lints}
-----------------------------------------------

* **markdownlint**: enforce headings/line length; allow tabs per your doctrine; permit fenced examples.

* **constitution_check.py** (tiny script):

    * Flags unfenced capture blocks in `docs/` (they must be fenced).

    * Greps for header lines in docs and ensures they live inside ``` fences.

    * Verifies Noise Budget hints are _not_ present in header lines.

* **pre‑commit** hook: runs `constitution_check.py`, `pytest -q` on parser tests, and `make harvest --dry-run` on a tiny sample log.


* * *

IX. Appendix — Canonical anchors {#anchors}
-------------------------------------------

* **Epistemic Design Brief** — provenance/time/observer as law (why provenance matters). epistemic_design_brief

* **SpecPrime Capture Contract v1** — exact parser surface (headings, header keys, BODY, updates). make_note

* **Delight Manifesto** — human engagement as a system input; bilingual doctrine. tone_design_manifesto


* * *

### One‑page TL;DR (paste at top of new repos)

> A repo is a **semantic field**.
> We write **specs for AI** (rich with intent) and **blocks for parsers** (cold and exact).
> Delight keeps humans engaged; provenance keeps machines honest.
> Friendly prompts compile to strict blocks.
> Warmth in human surfaces only; never in header lines.
> Append, don’t erase.
> If in doubt, add intent until a parser breaks—then back off one notch. tone_design_manifesto make_note epistemic_design_brief

* * *

If you want, I can also mint a **`constitution_check.py`** scaffold and a tiny **pre‑commit** block so this stays enforced by tooling, not just vibes.

* * *

**ChatGPT:**

Perfect. Here’s a **repo‑ready Constitution** plus a tiny enforcement script and Make targets. It encodes your “repo as semantic habitat” philosophy: **specs are for AI (rich and humane); blocks are for parsers (boring and exact).** It also makes naming/layout a first‑class carrier of your _mental ontology_, not just taxonomy. I’ve cross‑linked the three canonical anchors so this stays grounded: **Epistemic Design Brief** (provenance/time/observer), **SpecPrime Capture Contract v1** (strict block grammar), and the **Delight/Tone Manifesto** (warmth as a reliability feature). epistemic_design_brief make_note tone_design_manifesto

* * *

`docs/CONSTITUTION.md` — OughtWorks Repository Constitution (v1.2)
------------------------------------------------------------------

> **Thesis.** A repository is a **probabilistic bias field** for humans and models.
> Names, layout, comments, specs, and commit voice all bend the next‑token distribution.
> Our rule: **write specs for AI** (encode intent, context, and tone), then **compile blocks for parsers** (strict headers, fixed order).
> Provenance and time are law; delight keeps the human runtime online. epistemic_design_brief tone_design_manifesto

### Canonical anchors (do not drift)

* **Epistemic Design Brief** — provenance/time/observer as first‑class. Everything meaningful carries _who/when/source_. epistemic_design_brief

* **SpecPrime Capture Contract v1** — the **only** parser surface: headings, header keys, order, BODY delimiter, updates. Tooling targets this surface. make_note

* **Design Manifesto — Delight as a Design Primitive** — warmth in human surfaces is a reliability feature (and never in header lines). tone_design_manifesto


* * *

### I. Principles (the shape of our gravity well)

1. **Names encode ontology.** We treat identifiers as “cognitive fossils.” Variable/class/file names don’t just classify—they reveal the **mental model** that produced them. Code that reads like boilerplate will elicit boilerplate; names that show how we _think_ bias models toward creative association.

2. **Bilingual surfaces.** Human zones are warm, skimmable, invitational. Machine zones are strict, testable, and boring (on purpose). tone_design_manifesto

3. **Specs for AI; blocks for parsers.** The spec that teaches a model _what to write and why_ is rich and humane; the example blocks are cold and exact per the capture contract. make_note

4. **Provenance or it didn’t happen.** Most artifacts—design notes, audits, decisions—carry _time, source, and observer_. Append new truth; don’t rewrite history. epistemic_design_brief


* * *

### II. Laws (normative; enforce or explain)

**L1 — Naming Charter (mental ontology).**

* Prefer **verb–object** or **topic—angle** names that telegraph intent: `seed_hypothesis()`, `harvest_chat.py`, `tone_friction.md`.

* Avoid generic glue (`utils`, `misc`, `helpers`). If a name doesn’t teach, rename.

* Rename freely when the concept clarifies; the ontology is _alive_.


**L2 — Layout Charter (lab vs. factory).**

* Keep a visible split between **exploration** and **rigor** (e.g., `Playground/` vs `OughtCore/`). Exploration invites novelty; rigor keeps instruments calibrated.


**L3 — Spec Charter (for AI).**

* Design docs explain **intent, stakes, trade‑offs, and heuristics** in a warm register (Noise Budget ≈ 10–15%).

* Inside those docs, any **parser examples** are present but **cold** (fixed headings/keys/order) and fenced to avoid accidental harvest. make_note


**L4 — Capture Contract (for parsers).**

* In chats (or files meant for harvest), emitted blocks must strictly match **SpecPrime Capture Contract v1**. Don’t alter headings or key order; updates are append‑only and reference `REF_UUID`. make_note


**L5 — Noise Budget.**

* Human surfaces may carry **10–20%** warmth (metaphor, connective tissue).

* Machine surfaces (headers, schema fields, code syntax) carry **0%** warmth. Keep humor and emojis out of header lines. tone_design_manifesto


**L6 — Provenance Law.**

* Design decisions include date, author/agent, and a pointer to source (session id, file anchor, or commit). Timelines evolve via **append**, not overwrite. epistemic_design_brief


**L7 — Friendly commands must compile to strict blocks.**

* Natural prompts (“jot a note…”, “add a task…”, “mark done…”) **must** compile to the capture grammar. Then add a one‑line receipt (`CAPTURED: KIND UUID`). make_note


**L8 — Documentation ≠ parser input.**

* In repo docs, **fence** any capture examples (`…`); in chatlogs intended for harvest, keep blocks **unfenced**. Tooling should ignore fenced content. make_note


* * *

### III. Practices (how we keep the bias field healthy)

**P1 — File prologues that teach.**
At the top of nontrivial modules: “Problem this file solves. Invariant that must remain true.” One tight paragraph; no apologizing.

**P2 — Commit voice.**
Subjects are imperative and purposeful (≤72 chars), bodies say **why** and reference IDs. Voice should be kind, plain, and a bit playful—this repo _onboards minds_, not just machines.

**P3 — Reflection cadence.**
Every few commits, add a short `REFLECTION` (in Playground) linking to decisions, trade‑offs, and unknowns. Those bodies are hydration fuel for future models.

**P4 — Rename without guilt.**
When a name stops teaching your ontology, rename it. The git history captures why.

* * *

### IV. Guardrails & Checks (tools, not vibes)

**G1 — Constitution Check.**

* Docs must not contain **unfenced** capture blocks (avoid accidental harvest).

* Docs over N lines should show at least one of: `# Intent`, `# Why`, or `# Rationale`.

* Header keys (`UUID:`, `PROJECT:`, etc.) must not appear outside fences in `docs/`.


**G2 — Harvest Smoke.**

* `make harvest --month <YYYY-MM>` on a sample chat dir should yield ≥1 file in `Playground/notes|todos` and update a monthly index.


**G3 — Tone Ping.**

* Spot‑check long docs for monotone drift; sprinkle connective tissue back in if attention drops. Warmth is a design primitive. tone_design_manifesto


* * *

### V. Session Ritual (for AI collaborators)

At the start of a working chat, paste the hydrate card (SpecPrime v1.x). Expect an ACK with `session_id`, anchors, and `noise_budget`. Use friendly commands; receive strict blocks. End with a `SESSION-INDEX`. make_note

* * *

### VI. Governance & Versioning

* Constitutional PRs carry label `constitution`; include a short **delta** of which clauses changed and why.

* Bump version header (`v1.x`) and append a changelog entry.


* * *

### TL;DR for Future Contributors

* The repo is a **semantic habitat**.

* **Names teach ontology.** Layout shows where play vs. rigor live.

* **Specs teach AI with warmth; blocks feed parsers with precision.**

* **Provenance and time are law.** Delight keeps us here. epistemic_design_brief tone_design_manifesto


* * *

Minimal enforcement script — `tools/constitution_check.py`
----------------------------------------------------------

```python
#!/usr/bin/env python3
"""
Light constitutional checks:
- Warn on unfenced capture blocks in docs/ (## NOTE|TODO|REFLECTION...).
- Warn if header keys (UUID:, PROJECT:, TAGS:, CREATED_AT:) appear outside fences in docs/.
- Nudge long docs to include an 'Intent/Why/Rationale' section.
"""
import re, sys, pathlib

DOCS = pathlib.Path("docs")
CAPTURE_HEAD = re.compile(r"^##\s*(NOTE|TODO|REFLECTION|TODO-STATUS|NOTE-UPDATE)\s*—", re.M)
HEADER_KEYS = re.compile(r"^(UUID|PROJECT|TAGS|CREATED_AT|REF_UUID|PRIORITY|STATUS|DUE):", re.M)
WHY_HEAD = re.compile(r"(?mi)^\s{0,3}#{1,3}\s*(intent|why|rationale)\b")

def is_fenced(text: str, match_span: tuple[int,int]) -> bool:
    # crude: count triple-backtick fences above/below; odd count => inside fence
    start, _ = match_span
    above = text[:start]
    open_count = above.count("```")
    return (open_count % 2 == 1)

def scan(path: pathlib.Path) -> list[str]:
    issues = []
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return [f"ERR read {path}: {e}"]

    # 1) Unfenced capture headings
    for m in CAPTURE_HEAD.finditer(text):
        if not is_fenced(text, m.span()):
            issues.append(f"{path}: unfenced capture heading '{m.group(0).strip()}'")

    # 2) Header keys outside fences
    for m in HEADER_KEYS.finditer(text):
        if not is_fenced(text, m.span()):
            issues.append(f"{path}: header key outside fence '{m.group(0).strip()}'")

    # 3) Long doc w/o Intent/Why/Rationale
    if len(text.splitlines()) > 200 and not WHY_HEAD.search(text):
        issues.append(f"{path}: long doc lacks an Intent/Why/Rationale section")

    return issues

def main():
    if not DOCS.exists():
        print("docs/ not found; skipping.")
        sys.exit(0)
    problems = []
    for p in DOCS.rglob("*.md"):
        problems += scan(p)
    if problems:
        print("❌ Constitution check found issues:")
        for line in problems:
            print(" -", line)
        sys.exit(2)
    print("✅ Constitution checks passed.")
if __name__ == "__main__":
    main()
```

> It’s intentionally simple and fast: no external deps, just enough friction to keep the **bilingual split** and the **why‑sections** intact.

* * *

Makefile snippets (drop‑in)
---------------------------

```makefile
# --- Constitution & Harvest hygiene ---
PY ?= python3

check-constitution: ## Lint docs for unfenced blocks & missing Intent/Why
	@$(PY) tools/constitution_check.py

harvest-smoke: ## Run a tiny harvest smoke (customize month)
	@$(PY) tools/harvest_chat.py --month 2025-10 || true
```

Optional pre‑commit hook (manual install once):

```bash
cat > .git/hooks/pre-commit <<'SH'
#!/usr/bin/env bash
set -e
echo "🔎 Constitution checks…"
python3 tools/constitution_check.py
SH
chmod +x .git/hooks/pre-commit
```

* * *

(Optional) `.github/copilot-instructions.md` (repo‑level steering)
------------------------------------------------------------------

```md
# House Rules (OughtWorks)
- This repo treats **names as mental ontology**: prefer verb–object or topic—angle; avoid generic 'utils'.
- **Specs are for AI (warm, contextual); blocks are for parsers (strict).**
- When asked to “jot a note / add a todo / mark done,” compile to the capture grammar (SpecPrime v1).
- In human surfaces, keep ~15% connective tissue; in header lines, keep 0%.
- Prefer associative exploration first, narrow later; explain trade‑offs and rationale in one short paragraph.
```

* * *

### How to adopt (quick)

1. Save `docs/CONSTITUTION.md`.

2. Add `tools/constitution_check.py` and the Make targets.

3. (Optional) Add the repo‑level instructions file for your editor/assistant.

4. Commit with a tone that teaches:
    `docs: add Constitution — specs for AI, blocks for parsers; names encode ontology`


From here on, the repo itself _teaches_ every future contributor—human or model—to behave the way you intend: **creative by default, precise where it counts, and always provenance‑aware.** That’s the atmosphere you want the project to breathe. epistemic_design_brief make_note tone_design_manifesto

If you want, I can mint a tiny `CONTRIBUTING.md` that references this Constitution and shows the **naming Charter** with before/after examples for renames.
