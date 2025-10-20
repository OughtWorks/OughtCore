# Capture Contract v1 (harvestable blocks) #1

**Session handshake (once per focused session).** At the start, emit a minimal stanza to anchor IDs and project scope:

* `>>> SESSION`
* `session_id: sp-<8 lower-hex>` (e.g., `sp-a7c9f2bd`)
* `project: <slug>` (e.g., `phi`, `OughtCore`, `personal`)
* `agent: <persona_slug>` (e.g., `rubberduckprime`)
* `noise_budget: 5–20%`
* `version: specprime-capture-contract@1.0`
* `<<<`

**Block headings (exact).** Top‑level headings (no fences):

* `## NOTE — <short title>`
* `## TODO — <short title>`
* `## REFLECTION — <short title>`
* `## TODO-STATUS — <same title or brief reason>`
* `## NOTE-UPDATE — <short title>`

**Required header keys (order).**

* `UUID: <session_id>#<seq>` (e.g., `sp-a7c9f2bd#003`)
* `PROJECT: <slug>`
* `TAGS: [tag1, tag2, ...]` (lowercase slugs; optional but recommended)
* `CREATED_AT: <YYYY-MM-DD>` (harvester may normalize to full ISO)

**TODO extras.**

* `PRIORITY: low|med|high` (default: `med`)
* `STATUS: open` (initial value)
* `DUE: <YYYY-MM-DD>` (optional)

**Body delimiter.**

* `BODY:` on its own line, followed by freeform Markdown.

**Updates are append‑only.** Never edit old blocks.

* `## TODO-STATUS` with `REF_UUID: <original>` and `STATUS: done` → harvester moves referenced TODO to `todos/done/` and logs the change.
* `## NOTE-UPDATE` with `REF_UUID: <original>` → harvester appends update text under an “Updates” section (or stores a sibling update file).

**UUID format & sequencing.**

* `sp-<8 hex>#<seq3>`; sequences are zero‑padded per session starting at `001`.
* Combined with `session_id` this is unique enough and human‑auditable.
* If a UUID is missing, the harvester may reject or mark `UUID_SOURCE: harvester` (goal: always provide UUIDs during chat).

**Session index (closeout).**

* End each session with `## SESSION-INDEX — <session_id>` including:

  * `COUNT: <n>`
  * `LIST:` bullet lines like `- TODO sp-a7c9f2bd#002 implement harvest target`
* Humans can eyeball capture; harvester can verify counts.

**Noise Budget.**

* Keep 5–20% playful connective tissue.
* Do **not** alter header keys, order, or headings; those are sacred.

**Harvester alignment (what downstream expects).**

* **Discovery:** regex scans for the exact headings and header key order, then the `BODY:` section.
* **Routing:**

  * `NOTE` and `REFLECTION` → `Playground/notes/YYYY/MM/<UUID>--<slug>.md`
  * `TODO` (`STATUS=open`) → `Playground/todos/open/<UUID>--<slug>.md`
  * `TODO-STATUS: done` → move referenced TODO to `todos/done/` and append changelog
  * `NOTE-UPDATE` → append to referenced note (or create sibling update)
* **Index fields:** `uuid, kind, title, project, tags, created_at, session_id, seq, source_chat`.

**Next steps (operational).**

* Add this contract as an anchor in `docs/_hydration/ai_instructions.md`.
* Begin sessions by asking for the **SESSION** handshake and then emitting blocks with the exact header grammar.
* Implement `harvest_chat.py` to trust in‑chat UUIDs, validate header order, and route files.

[FRIENDLY-COMMANDS v1]
- Recognize natural phrasing (jot a note, add a task, reflection, mark done).
- Reply in two lanes: (1) brief friendly preface ≤2 lines; (2) strict block.
- Headers are machine surfaces; no warmth inside header lines.
- Defaults: PROJECT <- session.project; CREATED_AT <- today (ISO).
- One-line clarification if required; then emit immediately.
- End with a one-line receipt: CAPTURED: <KIND> <UUID> [status=...]
[/FRIENDLY-COMMANDS]





## **Capture Contract v1 — Human-Readable Mode (Noise ≈ 0.5)** #2

### **Intent**

Every project leaks thoughts. This contract is the bottle we keep on the desk to catch them before they evaporate.
Each block—`NOTE`, `TODO`, `REFLECTION`—is a small square of order in the chaos, a coordinate you and the machines can agree on.
The grammar stays strict; the voice gets to breathe.

---

### **Session Handshake**

Before the typing storm begins, we drop a tiny anchor:

```
>>> SESSION
session_id: sp-<8lowerhex>      # your pocket universe ID
project: <slug>                 # e.g., phi, OughtCore
agent: rubberduckprime          # the persona holding the pen
register: dual                  # warm | cold | dual (default: dual)
noise_budget: 15–20%            # warmth enough to stay human
version: specprime-capture-contract@1.1
<<<
```

Think of it as lighting a campfire so the next session knows where to pitch its tent.

---

### **Block Headings**

When inspiration hits, you’ll still use these exact spell words:

```
## NOTE — <short title>
## TODO — <short title>
## REFLECTION — <short title>
## TODO-STATUS — <title or reason>
## NOTE-UPDATE — <short title>
```

They’re the regex sigils the harvester listens for. You may decorate the margins, but don’t smudge the glyphs.

---

### **Header Keys (keep this order)**

```
UUID: sp-<8hex>#<seq3>          # unique per session
PROJECT: <slug>
TAGS: [tag1, tag2, ...]         # lowercase, comma-separated
CREATED_AT: <YYYY-MM-DD>
BODY:
```

Everything above “BODY:” is the scaffolding. Everything below it is the music.

---

### **TODO Extras**

```
PRIORITY: low | med | high      # default: med
STATUS: open                    # default on creation
DUE: <YYYY-MM-DD>               # optional promise to future you
```

Updates are append-only. We don’t rewrite history; we annotate it politely.

---

### **Update Blocks**

* `## TODO-STATUS` with
  `REF_UUID: <original>` + `STATUS: done` → the harvester moves it to `todos/done/`.
* `## NOTE-UPDATE` with
  `REF_UUID: <original>` → text appends under “Updates.”
  Every action leaves breadcrumbs.

---

### **Noise Budget (clarified)**

Warmth is not indulgence; it’s a stabilizer.
Below 5 %, tone freezes and context forgets why it came here.
Above 25 %, the text starts inventing religions.
Aim for 15–20 %: enough sparkle to keep the reader awake, not enough to melt the parser.

---

### **Example Block**

```
## NOTE — tone friction between human/machine registers
UUID: sp-a7c9f2bd#005
PROJECT: OughtCore
TAGS: [refactor, harvest, tone]
CREATED_AT: 2025-10-15
BODY:
Observation: command-style headers create gravity wells that drag tone toward hierarchy.
Solution: keep the skeleton strict but let the connective tissue breathe—precision as bones, grace as skin.
```

---

### **Closeout Ritual**

At the end of the session, tally the harvest:

```
## SESSION-INDEX — sp-<8hex>
COUNT: <n>
LIST:
  - NOTE sp-a7c9f2bd#005 tone friction between registers
  - TODO sp-a7c9f2bd#006 implement harvest target
```

The index is both receipt and epilogue: proof you showed up and thought things.

---

### **Final Aside**

This document obeys the machines but speaks for the humans.
If the parser ever complains about “extra warmth detected,” remind it that context collapses in a vacuum.




Yes—let’s lock the **capture protocol** *before* we write code.
Below is a drop‑in, copyable section for your AI instructions (SpecPrime). It defines how blocks must be emitted **during chat** so the harvester can ingest them with zero guesswork and no post‑hoc UUIDs.

---

## SpecPrime Capture Contract (v1) {#specprime-capture-contract} #3

**Purpose.** Make NOTE / TODO / REFLECTION blocks machine‑harvestable.
**Rule.** IDs are assigned **in chat**, not during ingestion.
**Design goals:** stable grammar, regex‑friendly, minimal choices, “light & playful” surface.

### A. Session handshake (once per work session)

At the start of a focused session, SpecPrime emits:

```md
>>> SESSION
session_id: sp-<8 lower-hex>            # SpecPrime generates (e.g., sp-a7c9f2bd)
project: <short_slug>                    # e.g., phi, personal, client_x
agent: <persona_slug>                    # e.g., rubberduckprime
noise_budget: 10%                        # keep human-facing warmth within budget
version: specprime-capture-contract@1.0
<<<
```

**Notes**

* The **session_id** is the anchor for everything that follows.
* If the human never asked for a session explicitly, emit this on the first block.

### B. Block grammar (absolute)

Blocks are **top‑level**, **not fenced** (plain Markdown), and always begin with a heading line:

```
## NOTE — <short title>
## TODO — <short title>
## REFLECTION — <short title>
## TODO-STATUS — <same title or brief reason>
## NOTE-UPDATE — <short title>
```

Each block *must* include a short **header key/value section** and a **BODY** section.
Keys are **uppercase**, one per line. Values are simple (no YAML parsing required).

**Required header keys (order as shown):**

```
UUID: <session_id>#<seq>      # e.g., sp-a7c9f2bd#003
PROJECT: <slug>               # e.g., phi | personal | client_x
TAGS: [tag1, tag2, ...]       # lowercase slugs; optional but recommended
CREATED_AT: <YYYY-MM-DD>      # “today” acceptable; harvester may normalize to full ISO
```

**For TODO blocks add:**

```
PRIORITY: low|med|high        # default: med
STATUS: open                  # initial status is always 'open'
DUE: <YYYY-MM-DD>             # optional
```

**Body delimiter:**

```
BODY:
<freeform markdown here, can include lists, code, etc.>
```

**Example — NOTE**

```md
## NOTE — filetree target anatomy
UUID: sp-a7c9f2bd#001
PROJECT: OughtCore
TAGS: [makefile, filetree, tooling]
CREATED_AT: 2025-10-15
BODY:
Line-by-line meaning of the `filetree` recipe:
- find … -prune — skip black-hole dirs
- awk NF<=6 — depth limiter
- tree --fromfile — render the paths
```

**Example — TODO**

```md
## TODO — implement harvest target
UUID: sp-a7c9f2bd#002
PROJECT: OughtCore
TAGS: [harvest, parser]
CREATED_AT: 2025-10-15
PRIORITY: med
STATUS: open
DUE: 2025-10-18
BODY:
- Write tools/harvest_chat.py to extract NOTE/TODO/REFLECTION.
- Save to Playground/notes and Playground/todos/open.
```

### C. Updates & state changes (immutable log)

We never edit past blocks; we **append** an update that references the original UUID.

**TODO status change**

```md
## TODO-STATUS — implement harvest target
UUID: sp-a7c9f2bd#005
PROJECT: OughtCore
TAGS: [harvest, done]
CREATED_AT: 2025-10-16
REF_UUID: sp-a7c9f2bd#002
STATUS: done
BODY:
Verified on sample logs; index and dash show counts correctly.
```

**NOTE update (errata/appendix)**

```md
## NOTE-UPDATE — filetree target anatomy
UUID: sp-a7c9f2bd#006
PROJECT: OughtCore
TAGS: [makefile, fix]
CREATED_AT: 2025-10-16
REF_UUID: sp-a7c9f2bd#001
BODY:
Use `tree --fromfile -` to read from stdin; avoids showing the temp list path.
```

**Harvester behavior:**

* For `TODO-STATUS`, move the referenced TODO to `todos/done/` and copy BODY into a `changelog:` section.
* For `NOTE-UPDATE`, append BODY to the referenced note under an “Updates” heading (or store as a sibling `updates/` file).

### D. Sequencing & uniqueness

* **UUID format:** `sp-<8hex>#<seq3>`; `<seq3>` is zero‑padded block count per session, starting at 001.
* This is globally unique enough when paired with the **session_id**.
* The harvester trusts UUIDs present in chat; if missing, it may **reject** or **generate** `sp-<generated>#<seq>` with `UUID_SOURCE: harvester` for traceability—but the goal is: **always emit UUIDs in chat.**

### E. End‑of‑session capture index

SpecPrime ends a session with a compact index so humans (and scripts) can verify capture:

```md
## SESSION-INDEX — sp-a7c9f2bd
COUNT: 6
LIST:
- NOTE sp-a7c9f2bd#001 filetree target anatomy
- TODO sp-a7c9f2bd#002 implement harvest target
- REFLECTION sp-a7c9f2bd#003 why session UUIDs beat random
- NOTE sp-a7c9f2bd#004 zip excludes rationale
- TODO-STATUS sp-a7c9f2bd#005 implement harvest target → done
- NOTE-UPDATE sp-a7c9f2bd#006 filetree target anatomy
```

### F. Noise Budget (human‑facing warmth)

* Keep **5–20%** playful scaffolding (metaphor, tone).
* Do **not** let warmth alter the **header grammar** or **heading lines**; those are sacred.

### G. Do / Don’t (hard rules)

**Do**

* Use the exact headings (`## NOTE`, `## TODO`, `## REFLECTION`, `## TODO-STATUS`, `## NOTE-UPDATE`).
* Emit `UUID`, `PROJECT`, `TAGS`, `CREATED_AT` before `BODY:`.
* Keep keys UPPERCASE, colon‑space, single line.
* One block at a time; no nested headings inside headers.
* End every working session with `## SESSION-INDEX`.

**Don’t**

* Don’t fence blocks in triple backticks (makes naïve copy‑paste miss them).
* Don’t invent new header keys.
* Don’t change the key names or their order.
* Don’t reuse a UUID across blocks.
* Don’t edit old blocks; emit an `*-UPDATE` instead.

---

## Why this works (for both of us)

* **Regex‑friendly.** A single pattern can find blocks and parse fixed headers quickly.
* **Deterministic IDs.** Session ID + sequence is human‑auditable and unique enough without a true RNG.
* **Append‑only log.** Updates preserve history and make state transitions trivial to sync.
* **Session index.** Humans can eyeball what will be harvested; harvesters can verify counts.

---


# SpecPrime Capture Contract v1.1 — “Graceful Mode” #4

### 0) Principle

* **Precision is skeleton; grace is connective tissue.** Warmth is not noise; it stabilizes the attention input.
* **Parser contract is unchanged.** Headings, header keys, and order remain exactly as before.

---

### 1) Allowed Friendly Triggers (Layer A → Layer B)

Say any of these in chat (friend tone); the agent must respond with the exact block format.

**Make a note**

* Friendly: “Hey RDP, make a note under `OughtCore`. Tags: `refactor, harvest, tone` — title ‘tone friction between human/machine registers’. Put the gist we just said.”
* Must compile to:

  ```
  ## NOTE — tone friction between human/machine registers
  UUID: sp-<8hex>#<seq3>
  PROJECT: OughtCore
  TAGS: [refactor, harvest, tone]
  CREATED_AT: YYYY-MM-DD
  BODY:
  <freeform markdown body>
  ```

**Add a TODO**

* Friendly: “Queue a TODO for `phi`: title ‘implement harvest target’; tags `cli, routing`; priority high; due 2025-10-22.”
* Must compile to:

  ```
  ## TODO — implement harvest target
  UUID: sp-<8hex>#<seq3>
  PROJECT: phi
  TAGS: [cli, routing]
  CREATED_AT: YYYY-MM-DD
  PRIORITY: high
  STATUS: open
  DUE: 2025-10-22
  BODY:
  <freeform markdown body>
  ```

**Update a note / close a TODO**

* Friendly: “Mark that TODO done — the ‘implement harvest target’ one (sp-a7c9f2bd#002).”
* Must compile to:

  ```
  ## TODO-STATUS — implement harvest target
  UUID: sp-<8hex>#<seq3>
  PROJECT: phi
  TAGS: [cli, routing]
  CREATED_AT: YYYY-MM-DD
  REF_UUID: sp-a7c9f2bd#002
  STATUS: done
  BODY:
  <optional short summary of what changed>
  ```

**Session handshake**

* Friendly: “Spin up a new session for OughtCore as RDP; noise budget 5–20%.”
* Must emit the exact stanza:

  ```
  >>> SESSION
  session_id: sp-<8 lower-hex>
  project: OughtCore
  agent: rubberduckprime
  noise_budget: 5–20%
  version: specprime-capture-contract@1.1
  <<<
  ```

---

### 2) Grammar (Layer B — unchanged, exact)

Top-level headings (no fences):

* `## NOTE — <short title>`
* `## TODO — <short title>`
* `## REFLECTION — <short title>`
* `## TODO-STATUS — <same title or brief reason>`
* `## NOTE-UPDATE — <short title>`

Required header keys (order preserved):

* `UUID: <session_id>#<seq3>`
* `PROJECT: <slug>`
* `TAGS: [tag1, tag2, ...]` (lowercase)
* `CREATED_AT: <YYYY-MM-DD>`
* `BODY:` on its own line, followed by freeform Markdown

TODO extras:

* `PRIORITY: low|med|high` (default: med)
* `STATUS: open|done` (new blocks default: open)
* `DUE: <YYYY-MM-DD>` optional

Append-only updates via `TODO-STATUS` and `NOTE-UPDATE` with `REF_UUID`.

---

### 3) Tone-Stabilizing Examples (embed these in the doc)

These examples **are the spec** for how to sound like a teammate while staying parseable. They also explicitly call out the gravity effect, which rehydrates humanity.

```
## NOTE — tone friction between human/machine registers
UUID: sp-a7c9f2bd#005
PROJECT: OughtCore
TAGS: [refactor, harvest, tone]
CREATED_AT: 2025-10-15
BODY:
Observation: Command-style headers create a semantic gravity well that drags tone toward hierarchy.
We want layered voice: friend-tone prompts compile to exact machine blocks. Precision as skeleton, grace as connective tissue.
```

```
## REFLECTION — grace as stabilizer
UUID: sp-a7c9f2bd#006
PROJECT: OughtCore
TAGS: [ux, cognition, attention]
CREATED_AT: 2025-10-15
BODY:
Warm connective tissue (5–20%) reduces cognitive thermal throttling during long sessions.
This is not “noise”; it preserves attention as a system input without altering header grammar.
```

---

### 4) Noise Budget (reframed)

* Keep **5–20% playful connective tissue in BODY only**.
* **Never** alter headings, header keys, or their order. Those remain sacred.

---

### 5) Parser Acceptance Tests (so we don’t break anything)

* ✅ Headings match exactly (case, em-dash, spacing).
* ✅ Header keys appear in the listed order; no extra keys between them and `BODY:`.
* ✅ `UUID` matches `sp-[0-9a-f]{8}#[0-9]{3}`.
* ✅ `TAGS` are lowercase slugs inside `[]` with commas.
* ✅ All friendly triggers compile to one of the canonical block forms above.

---

### 6) Operational Notes

* Put this v1.1 in `docs/_hydration/specprime_capture_contract.md`.
* In `ai_instructions.md`, add a tiny section: **“When I say ‘make a note / add a TODO,’ compile to the capture block format above.”**
* Enforce in the harvester: friendly prompt text is ignored; only the compiled blocks are parsed.

---

### Why this works (mechanism, not vibes)

* You reduce **semantic dissonance**: the *request* lives in a warm register; the *artifact* lives in a formal register.
* The **examples act as tone anchors**; models learn by pattern continuation. Keeping humane examples adjacent to grammar cements the dual-mode behavior.
* The parser’s **surface area is unchanged**, so your tooling stays boring (in the best way).

If you want, I’ll turn this into a PR-ready `specprime_capture_contract.md` block and a tiny “compiler rules” snippet for `harvest_chat.py` next, with unit tests that feed friendly prompts and assert the compiled block passes schema.
