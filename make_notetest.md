Here is a draft of your **Capture Contract Spec**, fully aligned with the principles of Nomena’s Constitution and Document Design Guide. It teaches both models and humans how to consistently generate harvestable knowledge blocks from chat with minimal cognitive friction.

---

# Capture Contract — Ritual for Semantic Block Harvest

## Intent

This spec formalizes the contract between human cognition and machine organization during creative chat sessions. It solves the problem of fleeting insight by codifying a ritual: model-generated blocks that are immediately harvestable, classifiable, and semantically tagged—without human overhead.

## Context

In fast-paced ideation, insights often die in chat history. Organizing them steals attention from action. This spec shifts that labor onto the model, guiding it to output semantically tagged, properly structured blocks upon request. Humans focus on ideas; models handle capture.

## Doctrine

This document manifests:

* **Ontology in Names** — Every block header reveals function (`## NOTE`, `## TODO`, etc.).
* **Bilingual Surfaces** — Cold schemas inside; warm rationale around.
* **Append-Only Cognition** — Updates extend original entries; nothing is rewritten.
* **Teach Why Before How** — This contract explains its purpose before defining mechanics.
* **Transparency is Law** — Every block shows purpose, tags, UUID, and context.

---

## Specification (Cold Zone)

### Session Handshake

```
>>> SESSION
session_id: sp-<8lowerhex>      # your pocket universe ID
project: <slug>                 # e.g., phi, OughtCore
agent: rubberduckprime          # persona holding the pen
register: dual                  # warm | cold | dual
noise_budget: 15–20%            # warmth level for non-cold text
version: specprime-capture-contract@1.1
<<<
```

---

### Block Header Types

```
## NOTE — <short title>
## TODO — <short title>
## REFLECTION — <short title>
## TODO-STATUS — <short title or reason>
## NOTE-UPDATE — <short title>
```

---

### Header Keys (fixed order)

```
UUID: sp-<8hex>#<seq3>          # unique per session
PROJECT: <slug>
TAGS: [tag1, tag2, ...]         # lowercase, comma-separated
CREATED_AT: <YYYY-MM-DD>
BODY:
```

---

### TODO Extras (optional, strict keys)

```
PRIORITY: low | med | high      # default: med
STATUS: open                    # default
DUE: <YYYY-MM-DD>               # optional
```

---

### Update Blocks

```
## TODO-STATUS — <title or reason>
REF_UUID: <original UUID>
STATUS: done
```

```
## NOTE-UPDATE — <short title>
REF_UUID: <original UUID>
BODY:
<append-only content>
```

---

### Closeout Ritual

```
## SESSION-INDEX — sp-<8hex>
COUNT: <n>
LIST:
  - NOTE sp-xxxxxxx#001 short title
  - TODO sp-xxxxxxx#002 short title
```

---

## Pedagogy (Warm Zone)

Each block type channels a different kind of cognition:

* `## NOTE`: captures ambient insights or explanations.
* `## TODO`: encodes actionable items, ready for automation.
* `## REFLECTION`: records lessons, patterns, or anomalies noticed.
* `## TODO-STATUS`: signals completion; only valid with `REF_UUID`.
* `## NOTE-UPDATE`: appends context to a living note without overwriting it.

Tags should be **semantic**, not merely contextual. If a note explains a UX issue about a Git hook, use `[ux, hooks, friction]`—not `[issue, today, chat]`.

Session handshakes act like namespace declarations; they help future harvesters organize outputs by intent and identity.

The `SESSION-INDEX` is your final tally. It declares what was created and where to look.

---

## Ritual / Usage

When a user asks for a block (e.g., "turn that into a TODO"), the model emits a cold block using the strict template. The `UUID` must be unique per session. All updates preserve the original and reference it by `REF_UUID`.

Use append-only updates. Never overwrite or replace.

Human tone may guide, contextualize, or explain blocks—but must never drift inside the fenced syntax.

---

## Appendices

### Alignment Table

| Axiom                 | Manifestation                                    |
| --------------------- | ------------------------------------------------ |
| Ontology in names     | Block types encode intent (`NOTE`, `TODO`, etc.) |
| Bilingual surfaces    | Cold headers and warm narration coexist          |
| Transparency is law   | Every block declares purpose, project, and tags  |
| Append-only cognition | Notes and todos updated via `-UPDATE` forms      |
| Teach why before how  | Spec begins with Intent and Context              |

---

### Related

* `nomena_constitution.md`
* `nomena_doc_design_guide.md`
* `hydration_history.md` (if versioning block templates)

---

### Version

```
version: specprime-capture-contract@1.1
author_agent: rubberduckprime
created_at: 2025-10-16
```

---

Let me know if you'd like this turned into a Markdown file, or want a variant tuned for different kinds of block styles (e.g., journal-style, git-comment style, etc).
