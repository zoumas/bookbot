# Implementation Plan: Refactor Stats Module

**Branch**: `004-refactor-stats-module` | **Date**: 2026-07-17 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/004-refactor-stats-module/spec.md`

## Summary

Move `get_num_words(text)` out of `main.py` into a new `stats.py` module.
Update `main.py` to import it via `from stats import get_num_words`, with no
change to program output.

## Technical Context

**Language/Version**: Python 3 (3.14.6 locally)

**Primary Dependencies**: None (standard library module/import system only)

**Storage**: N/A

**Testing**: None introduced by this feature; correctness is verified by
`bootdev run <id>` / `bootdev run <id> -s` and manual `python3 main.py`,
comparing output to the pre-refactor run.

**Target Platform**: Local developer machine (Linux/macOS/WSL2), CPython 3

**Project Type**: Single-package script (two Python files, same directory)

**Performance Goals**: N/A — no logic changes, only relocation

**Constraints**: Output must be byte-for-byte identical to before the
refactor; no duplicate definition of `get_num_words` may remain in `main.py`

**Scale/Scope**: Two files (`main.py`, new `stats.py`); one function moved

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Lesson Fidelity** — PASS. Module name `stats.py` and import statement
  `from stats import get_num_words` match the lesson verbatim.
- **II. YAGNI / Course-Paced Simplicity** — PASS. Only the one function the
  lesson names moves; `get_book_text` and `main` stay put, no speculative
  further splitting.
- **III. Standard Library Only** — PASS. Uses Python's built-in module/import
  system only.
- **IV. Incremental, Non-Destructive Growth** — PASS. This is the textbook
  case for this principle: existing behavior is preserved exactly while
  organization improves.
- **V. Readability Over Cleverness** — PASS. Explicit named import, no
  wildcard import, per the lesson's own guidance.

No violations. Complexity Tracking table is not needed.

## Project Structure

### Documentation (this feature)

```text
specs/004-refactor-stats-module/
├── plan.md              # This file
├── quickstart.md         # Phase 1 output
└── tasks.md              # Phase 2 output (/speckit-tasks - not yet created)
```

research.md, data-model.md, and contracts/ are intentionally omitted: no
unresolved unknowns, no data entities, and the only "interface" change is an
internal Python import, not an external contract.

### Source Code (repository root)

```text
main.py    # get_book_text(path), main() — imports get_num_words from stats
stats.py   # get_num_words(text) — moved here unchanged
```

**Structure Decision**: Two flat files at the repository root, matching the
lesson's explicit `main.py` / `stats.py` split. No `src/` package layout yet
— still too small to warrant it, and the lesson doesn't ask for one.

## Complexity Tracking

*Not applicable — no constitution violations.*
