# 🧭 Capture Contract v2 — Nomena Edition
*A bilingual specification for autonomous note capture and semantic harvesting*

---

## Intent — Why This Exists

Human attention leaks.
Thoughts appear mid-conversation, then evaporate under the weight of “I’ll file that later.”
The **Capture Contract** is the structural answer to that entropy: a shared grammar between human and AI that converts *fleeting cognition* into *durable knowledge*.

This document teaches two audiences at once:

* **Machines:** how to identify, parse, and route capture blocks with exact reproducibility.
* **Minds:** how to phrase, tag, and title ideas so their future meaning stays discoverable.

It encodes Nomena’s constitutional doctrines:

- **Ontology in names** → Titles and tags reveal *intent*, not just topic.
- **Bilingual surfaces** → Cold scaffolds for parsers, warm rationale for humans.
- **Transparency is law** → Every thought has an address (`UUID`) and provenance (`session_id`).
- **Append-only cognition** → We never rewrite past reasoning; we layer understanding.

---

## Cognitive Roles — What Each Block Means

| Block Type | Cognitive Function | Use When… | Example Judgment |
|-------------|-------------------|------------|------------------|
| `NOTE` | Captures an *observation or definition* | You’ve learned or realized something | “This explains why X behaves like Y.” |
| `TODO` | Operationalizes an *intention* | You decide to act later | “Build validator for new schema.” |
| `REFLECTION` | Records *evaluation or meta-learning* | You’ve completed or reconsidered something | “That naming convention improved clarity.” |
| `TODO-STATUS` | Updates a task’s state | You finish or defer it | “STATUS: done.” |
| `NOTE-UPDATE` | Extends an existing note | You add context or corrections | “Adding insight from later session.” |

---

## Session Handshake — The Campfire

Every focused collaboration starts by declaring its local universe:

```

> > > SESSION
> > > session_id: sp-<8lowerhex>       # Unique anchor for this creative run.
> > > project: <slug>                  # e.g., phi, Nomena, personal.
> > > agent: <persona_slug>            # The AI identity active in this session.
> > > register: dual                   # warm | cold | dual (default: dual).
> > > noise_budget: 15–20%             # Allowed warmth in body prose.
> > > version: nomena-capture-contract@2.0
> > > <<<

```

This stanza is a handshake between memory and intention.
It tells downstream systems how to thread everything that follows.

---

## Block Grammar — How Form Teaches Function

Every capture block begins with a top-level heading.
The heading *names the cognitive act*; the header keys *explain its ontology*.

### Headings (exact spellings)

```

## NOTE — <short title>

## TODO — <short title>

## REFLECTION — <short title>

## TODO-STATUS — <title or reason>

## NOTE-UPDATE — <short title>

```

Titles should declare purpose, not poetry.
A reader should grasp *what this block does* without opening it.

---

### Header Keys (fixed order)

```

UUID: sp-<8hex>#<seq3>      # Traceability anchor; every thought has an address.
PROJECT: <slug>             # Scope boundary; tells the harvester where this belongs.
TAGS: [tag1, tag2, ...]     # Semantic keys; describe meaning, not location.
CREATED_AT: <YYYY-MM-DD>    # Temporal anchor; supports chronological reasoning.
BODY:                       # Below this line lives the warm, human prose.

```

These keys are the skeleton.
The comments beside them are the anatomy notes that teach any model *why* they exist.

---

### TODO-Specific Fields

```

PRIORITY: low | med | high     # Helps focus attention; defaults to med.
STATUS: open                   # Initial condition; changed via TODO-STATUS.
DUE: <YYYY-MM-DD>              # Optional promise to future self.

```

---

## Behavioral Clause — How an AI Should Decide

When asked to capture, the AI:

1. **Determines block type** by cognitive role (observation → NOTE, action → TODO, evaluation → REFLECTION).
2. **Infers title** that communicates intent at a glance.
3. **Selects tags** representing conceptual meaning (e.g., `workflow`, `naming`, `tone`), not context like `chat`.
4. **Writes body** in natural Markdown within noise budget (≈15–20 % warmth).
5. **Emits** the cold header and warm body exactly as shown.

---

## Append-Only Updates

History is cumulative, never rewritten.

* `## TODO-STATUS` with
  `REF_UUID: <original>` + `STATUS: done` → harvester moves task to `todos/done/`.
* `## NOTE-UPDATE` with
  `REF_UUID: <original>` → appends update under “Updates” section or sibling file.

---

## Lifecycle — From Thought to Record

```

creation → capture → harvest → sort → evolve

```

1. **Creation:** Thought arises in chat.
2. **Capture:** AI emits structured block.
3. **Harvest:** Script extracts and validates blocks.
4. **Sort:** Harvester routes files by type, date, and project.
5. **Evolve:** Updates and reflections extend meaning.

---

## Tag Philosophy — The Semantics of Search

Tags are miniature ontologies.
They describe *what a note is about conceptually*, not *where* or *when* it was made.

- Use lowercase nouns or short noun phrases (`ontology`, `workflow`, `tone`, `api`).
- Avoid procedural tags like `meeting`, `chat`, `random`.
- Reuse tags across projects to create cross-domain connective tissue.

Tags are the relational glue of your cognitive graph.

---

## Example — Warm Core, Cold Edges

```

## NOTE — tone alignment between human and machine registers

UUID: sp-a7c9f2bd#005
PROJECT: Nomena
TAGS: [design, tone, capture]
CREATED_AT: 2025-10-16
BODY:
Observation: strict command headers create gravity wells that pull tone toward rigidity.
Remedy: keep the scaffolding cold but weave short rationale lines between keys.
Reasoning: precision is the bone; curiosity is the muscle; warmth keeps them from ossifying.

```

This block is simultaneously valid for a parser **and** instructive for a reader.
It models the dialect this spec teaches.

---

## Closeout Ritual — Index of Thought

At the end of a session, declare what was caught:

```

## SESSION-INDEX — sp-<8hex>

COUNT: <n>
LIST:

* NOTE sp-a7c9f2bd#005 tone alignment between registers
* TODO sp-a7c9f2bd#006 implement harvest target

```

This index is both a checksum for machines and a table of contents for minds.

---

## Alignment with the Nomena Constitution

The Capture Contract operationalizes the Constitution’s axioms:

| Constitutional Law | Manifestation in this Spec |
|--------------------|-----------------------------|
| Ontology in names | Block titles and tags encode purpose |
| Bilingual surfaces | Cold keys + warm body |
| Transparency | UUIDs, sessions, provenance |
| Append-only cognition | Updates, never edits |
| Teach why before how | Embedded semantic comments and rationale |

Together they ensure that **every captured idea carries both its coordinates and its conscience.**

---

## TL;DR

> The Capture Contract is a grammar for catching thought.
> Its headers keep machines precise; its bodies keep humans awake.
> Use it to make every fleeting idea addressable, interpretable, and alive.
