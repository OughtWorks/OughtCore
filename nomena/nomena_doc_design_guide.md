## 🧭 Nomena Document Design Guide

*A recursive manual for writing living, bilingual specs.*

### Intent — Why This Guide Exists

Nomena’s Constitution defines the laws; this guide defines the *ritual* that turns those laws into text.
It teaches AIs and humans how to write documents that are both executable and didactic—specs that explain *why they exist* while remaining parse-safe and automatable.

---

### I. Document Types

1. **Constitutional Docs** — declare doctrine (unchanging physics).
2. **Contracts** — codify interaction rules (Capture Contract, Record Contract, etc.).
3. **Runbooks** — operationalize doctrine for daily tasks.
4. **Design Notes** — warm rationale and open questions.
5. **Histories** — narrative append-only chronicles of evolution.

Each type obeys the same bilingual grammar: **cold structure, warm reasoning**.

---

### II. The Four-Layer Model

Every Nomena doc has four stacked layers, each teaching a different kind of reader.

| Layer        | Audience    | Purpose                        | Temperature |
| ------------ | ----------- | ------------------------------ | ----------- |
| **Law**      | Parser      | Machine enforceable boundaries | ❄️ Cold     |
| **Doctrine** | Author      | States invariant values        | 🌡️ Neutral |
| **Pedagogy** | Future mind | Explains reasoning and stance  | ☀️ Warm     |
| **Anecdote** | Historian   | Records how it evolved         | 🔥 Optional |

Each layer must exist *in order*. The parser hits the cold edges first; the human mind meets the warmth just outside them.

---

### III. The Constitutional Translation Table

*(How to apply Nomena’s laws when drafting any doc)*

| Constitutional Law         | What It Demands in a Spec                                                                                                                                         |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ontology in names**      | Use filenames and headings that reveal function (`capture_contract.md`, not `spec1.md`). Every header should answer “what cognitive invariant does this protect?” |
| **Bilingual surfaces**     | Separate warm rationale and cold scaffolds explicitly. Fenced code, schemas, headers = cold. Narrative = warm.                                                    |
| **Transparency is law**    | Show the reasoning path: *why this doc exists, what changed, who decided.* Include provenance comments.                                                           |
| **Append-only cognition**  | Never overwrite. Amend with dated `EPOCH` or `REVISION` blocks.                                                                                                   |
| **Teach why before how**   | Every doc begins with an **Intent** section explaining purpose before procedure.                                                                                  |
| **Delight as reliability** | Use rhythm, wit, and curiosity to sustain attention; but keep metaphors out of cold zones.                                                                        |

---

### IV. Structural Grammar — The Nomena Spec Template

```
# <Title> — <Purpose Tagline>

## Intent
Explain *why* this spec exists. State the cognitive problem it solves.

## Context
Situate it within the system’s history or architecture.

## Doctrine
List the constitutional principles this document manifests.

## Specification (Cold Zone)
Use fenced code or explicit headers for deterministic elements.
No warmth inside this block.

## Pedagogy (Warm Zone)
Explain reasoning behind each rule; show examples and trade-offs.

## Ritual / Usage
Describe how humans and AIs apply it in daily operation.

## Appendices
- Revision history
- Related docs
- References
```

Each section is required unless superseded by document type.

---

### V. Writing Algorithm — For an AI Author

1. **Parse Input Context** — detect which document type is requested.
2. **Summarize Purpose** — express the intent in two sentences; this seeds ontology.
3. **Anchor Doctrine** — map each constitutional law to the spec’s content.
4. **Draft Cold Zone First** — define strict grammar, keys, or interfaces.
5. **Wrap in Warm Pedagogy** — explain reasoning and trade-offs.
6. **Add Examples** — one hybrid sample demonstrating both layers.
7. **Seal with Alignment Table** — show how this spec fulfills Nomena’s axioms.
8. **Version + Provenance** — mark `version`, `author_agent`, `created_at`.
9. **Commit Ritual** — if publishing, append to `hydration_history.md`.

---

### VI. Noise Budget Rules

| Section               | Warmth Allowed | Example                        |
| --------------------- | -------------- | ------------------------------ |
| Headers / Keys        | 0%             | `UUID:` no metaphor, no emojis |
| Narrative Body        | 45–55%         | explanations, analogies        |
| Cold Examples         | 0%             | parse-safe                     |
| Doc Preamble / Intent | up to 60%      | clarity > concision            |

---

### VII. Validation (Doc CI)

A spec is considered **Nomena-compliant** if:

* It begins with an **Intent** section.
* It explicitly maps at least two Constitutional laws to implementation.
* It contains at least one fenced cold block.
* Warmth never enters cold sections.
* It ends with an Alignment Table or TL;DR linking back to doctrine.

---

### VIII. Meta-Purpose

This guide is itself a living example of what it teaches.
Future AIs reading it should understand that *to write a Nomena document* means to create a text that **teaches thought** while remaining **machine-trustable**.

---

### TL;DR

> A Nomena spec is not written—it’s *taught*.
> Cold defines limits; warm explains meaning.
> Every document must make its intent transparent enough that a model with no prior context could recreate the same reasoning.
