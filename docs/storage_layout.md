# Storage Layout (OughtCore)

**Goal:** keep OughtCore portable and self-contained across projects.

ProjectRoot/
└── .z_bootstrap/
├── z_ai_bootstrap/ -> symlink to ~/Projects/OughtCore
└── z_notes/ (local only; ignored)

markdown
Copy code

**Rules**
- `.z_bootstrap/` must be in the project's `.gitignore`.
- All OughtCore scripts use relative paths inside `z_ai_bootstrap/`.
- `out/` is ephemeral; safe to delete anytime.

**Acceptance**
- Running `make dash` in OughtCore prints a color message.
- Symlinked into a project, `make -C .z_bootstrap/z_ai_bootstrap dash` works from that project root.
