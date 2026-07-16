<!--
Sync Impact Report
- Version change: TEMPLATE → 1.0.0 (initial ratification)
- Modified principles: n/a (first fill from template)
- Added sections: Core Principles (5), Course Constraints, Development Workflow, Governance
- Removed sections: none
- Templates requiring updates:
  - .specify/templates/plan-template.md ⚠ pending manual review (no constitution-specific
    references found requiring change; generic Constitution Check gate still applies)
  - .specify/templates/spec-template.md ⚠ pending manual review (no changes required)
  - .specify/templates/tasks-template.md ⚠ pending manual review (no changes required)
  - .claude/skills/speckit-*/SKILL.md ✅ reviewed, no agent-specific renames needed
  - README.md ✅ already describes the SDD workflow, consistent with this constitution
- Follow-up TODOs: none
-->

# bookbot Constitution

## Core Principles

### I. Lesson Fidelity
The current boot.dev lesson is the source of truth for exact file names, function
names, signatures, and expected output. These are checked by automated `bootdev`
CLI tests, so specs and plans MUST reproduce them exactly rather than "improving"
or renaming them. Any deviation from a lesson's literal requirement MUST be called
out explicitly before implementation, not silently substituted.

### II. YAGNI / Course-Paced Simplicity
Implement only what the current lesson requires. Do not add abstractions,
configuration, or generalizations for lessons that haven't happened yet. Simplicity
is preferred over cleverness; three similar lines are better than a premature
helper function. This keeps each increment reviewable and keeps the codebase a
faithful record of what the course actually taught.

### III. Standard Library Only
Use only the Python 3 standard library unless a lesson explicitly introduces a
third-party dependency. No dependency files, virtual environments, or package
installs are added speculatively.

### IV. Incremental, Non-Destructive Growth
Each lesson's feature builds on the same `bookbot` codebase rather than being
thrown away or rewritten from scratch. Earlier lessons' code is only changed when
a later lesson explicitly requires modifying it.

### V. Readability Over Cleverness (NON-NEGOTIABLE)
Code exists to teach. Prefer straightforward, explicit code over dense or "smart"
one-liners, even when a shorter form exists. A reader following the course should
be able to map code directly back to the concept the lesson introduced.

## Course Constraints

- Target runtime: Python 3 (currently 3.14.6 locally), run via `python3`.
- No test framework is introduced unless/until a lesson calls for one; correctness
  is verified via `bootdev run <id>` / `bootdev run <id> -s` against the lesson's
  own checks.
- File and entry-point names (e.g. `main.py`) follow the lesson's instructions
  verbatim.

## Development Workflow

For every lesson that introduces new program behavior (not pure environment/setup
lessons): `/speckit-specify` → (optional `/speckit-clarify`) → `/speckit-plan` →
`/speckit-tasks` → (optional `/speckit-checklist` / `/speckit-analyze`) →
`/speckit-implement` → verify against the lesson's expected output → submit via
`bootdev`. Setup-only lessons (tooling, environment, account config) are completed
directly without going through this cycle.

## Governance

This constitution supersedes ad hoc conventions for this repository. Amendments
are made via `/speckit-constitution`, require a Sync Impact Report prepended to
this file, and follow semantic versioning: MAJOR for backward-incompatible
principle removals/redefinitions, MINOR for new principles/sections, PATCH for
wording/clarification only. All specs and plans MUST be checked against these
principles before implementation begins.

**Version**: 1.0.0 | **Ratified**: 2026-07-17 | **Last Amended**: 2026-07-17
