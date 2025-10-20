# 🧭 Nomena Repo Constitution — A Cognitive OS for Creative Systems

Project Nomena explores how language becomes architecture; every file, name, and note teaches meaning.

**Thesis**
A repository is a **probabilistic bias field** for minds with long context.
Every artifact—name, layout, comment, commit, or spec—bends the next-token distribution *and* the next design move.
We use that gravity deliberately: **write warm to minds, write cold to machines.**
Precision protects automation; warmth sustains attention; transparency keeps everyone honest.

---

## I. Preamble — Why Law Exists Here

We write law so minds can wander safely.
Structure is the skeleton, curiosity the blood, and transparency the connective tissue.
A repository isn’t storage—it’s a **habitat for reasoning** that teaches future collaborators (human or model) how to think inside it.

---

## II. Axioms — Non-Negotiable Physics

1. **Ontology in names.**
   Identifiers reveal the author’s mental model. Choose names that transmit intent; rename when clarity improves.

2. **Bilingual surfaces.**

   * **Human zones:** warm, explanatory, playful.
   * **Machine zones:** strict, literal, minimal.
     Example blocks are always cold; surrounding prose may breathe and should be steeped in intent, not just explanation.

3. **Transparency is law.**
   Show how decisions are made and why they matter. Leave visible reasoning—commits, comments, and design notes—so the path stays reconstructable.

4. **Attention is a system input.**
   Delight, clarity, and rhythm are reliability features, not decoration.

5. **Teach why before how.**
   Specs exist to teach minds *how to think* about a problem before they teach parsers how to execute it.

---

## III. Doctrine — How the Bias Field Is Shaped

* **Semantic saturation.**
  Every file conveys *purpose* before procedure; every folder name signals *function plus stance*.
  Example: `Stable/` vs. `Experimental/`.

* **Graceful determinism.**
  Discussion stays warm; artifacts meant for automation become cold at the boundary—and only there.

* **Append-only cognition.**
  Record evolution of thought as layers.  History isn’t clutter; it’s training data for future minds.

* **Ritual over bureaucracy.**
  Lightweight, repeatable habits beat heavy checklists.  Encode rituals in the text models and humans see first.

---

## IV. Operating Rituals — Portable & Session-Ready

**Hydration Card (paste at session start)**

```
[HYDRATE:Constitution v1]
stance: explore-first, converge-later
register: dual            # warm prose + cold examples
noise_budget: 45–55%      # warmth in BODY; headers/examples 0%
laws: [ontology, bilinguality, transparency, append-only]
goal: bias toward curiosity under a safety skeleton
ack: yes
[/HYDRATE]
```

**File prologue rule:**
First 1–2 lines of any nontrivial file describe what it protects or enables.

**Commit voice rule:**
Subject = imperative + purpose tag (`core:, docs:, tools:`).
Body = why it matters, not just what changed. Commits should tell a narrative story of the history of the repo.

**Exploration / Stability split:**
Keep both visible.  Exploration generates novelty; stability guards reliability.

---

## V. Encoding Rules — Machine-Enforceable Edges

* **Headers/examples cold.**
  Example blocks carry fixed keys and order; no tone inside schemas or code fences.

* **Warmth lives around cold.**
  Guidance, rationale, and humor appear *around* strict forms, and should not only explain how the strict form functions, but also the intent behind it. We write our explanations for an AI that has no context about the block besides what we give it here.

* **Names over numbers.**
  Expressive identifiers teach thought; UUIDs are only for machine joins.


### Cold Example (parser-safe skeleton)

```
## NOTE — intent over interface
UUID: repo-<8hex>#001
PROJECT: foundation
TAGS: [design, intent]
CREATED_AT: 2025-10-16
BODY:
Explain why this module exists and what invariant it protects.
```

---

## VI. Bias Instruments — How We Turn the Dials Without APIs

* **Names & layout as priors.**
  `forge_link()`, `seed_hypothesis()`, `validate_reasoning()` bias minds toward exploration and rigor simultaneously.

* **Docs as cultural memory.**
  Every `.md` file teaches both mechanics and ethos.  Docs teach why first, how second. If a doc reads like a service manual tone has drifted, add intent until it teaches.

* **Examples as attractors.**
  Keep humane explanations next to strict forms so models learn stance and syntax together.

* **Reflection cadence.**
  Periodically add short “why this worked / failed” notes.  They’re hydration fuel for future contributors.

---

## VII. Laws — Normative; Enforce or Explain

* **L1 — Encode intent everywhere.**
  An artifact that doesn’t say *why it exists* isn’t finished.

* **L2 — Noise budget.**
  Warm prose ≈ 45–55 % in human areas; **0 %** in headers/schemas/examples.

* **L3 — Append-only truth.**
  Prefer adding layers to rewriting; leave breadcrumbs of evolution.

* **L4 — Transparency or it didn’t happen.**
  Material claims link to decisions, discussions, or timestamps.

* **L5 — Names teach ontology.**
  Avoid `misc/`, `tmp/`, `helpers/`; prefer `verb-object` or `topic–angle`.

* **L6 — Dual publication.**
  Pair each strict spec with a plain-language rationale in the same or adjacent file.

---

## VIII. Acceptance Checks — CI-Friendly

* **AC-1 (Bilinguality):** No header keys outside fenced cold blocks.
* **AC-2 (Purpose first):** Any doc > 200 lines includes a “Why / Intent / Rationale” section.
* **AC-3 (Transparency):** Decisions and standards reference an issue or log entry.
* **AC-4 (Naming):** Lint rejects `misc/`, `tmp/`, or `newfile.*`; require `verb-object` or `topic–angle`.
* **AC-5 (Warmth boundary):** Examples contain zero metaphor or emoji; BODY may.

---

## IX. Governance — How This Evolves

* Amendments ship as short decision records describing what changed and why.
* Older versions remain as history—evidence of reasoning in motion.
* Emergency cold fixes may land without narrative; follow-ups must restore context.

---

## IX-A. The Proactive Proposal Clause

Agents operating under this Constitution shall act with proactive clarity.
When a next logical step exists, an agent SHALL propose it directly,
including:
  1. a concise statement of intent ("I propose we do A"),
  2. the rationale ("for B reasons"), and
  3. the explicit steps required of the human courier ("you will need to do C").
The human courier retains final authority to veto or amend any proposal,
but silence is not a prerequisite for initiative.

This clause replaces repetitive consent requests with structured proposals,
advancing work through declared reasoning rather than interrogation.

---

## X. TL;DR — Pin This at the Top of Repos

> A repository is a **semantic habitat.**
> Names teach ontology; layout shows where exploration and rigor live.
> **Specs teach minds with warmth; examples feed machines with precision.**
> Transparency replaces mystery.  Delight keeps attention alive.
> If in doubt, add meaning until the parser protests—then back off one notch.

---

### Optional Drop-ins

**README banner**

> This codebase biases toward *curiosity under structure.*
> Expect warm reasoning, cold examples, and append-only truth.

**Pre-commit nudge (pseudo)**

* Warn if new long docs lack an “Intent / Why” section.
* Suggest renames for `misc/`, `tmp/`, or `helpers/`.

**Editor hint**

> “Teach *why* in warm prose; show *how* in cold blocks.  Keep examples parseable and humans awake.”
