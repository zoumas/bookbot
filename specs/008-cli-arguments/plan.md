# Implementation Plan: CLI Arguments

**Branch**: `008-cli-arguments` | **Date**: 2026-07-17 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/008-cli-arguments/spec.md`

## Summary

Import `sys` in `main.py`. In `main()`, replace the hardcoded book path with
`sys.argv[1]`, guarded by a check that `len(sys.argv) < 2` prints the usage
message and calls `sys.exit(1)` before doing anything else. Validate against
`books/frankenstein.txt`, `books/mobydick.txt`, and
`books/prideandprejudice.txt`.

## Technical Context

**Language/Version**: Python 3 (3.14.6 locally)

**Primary Dependencies**: None (standard library `sys` module)

**Storage**: Local filesystem — reads whichever book path is passed as an
argument

**Testing**: None introduced by this feature; correctness is verified by
`bootdev run <id>` / `bootdev run <id> -s` and manual runs against all three
book files.

**Target Platform**: Local developer machine (Linux/macOS/WSL2), CPython 3

**Project Type**: Two-file script (`main.py`, `stats.py`)

**Performance Goals**: N/A — same per-book cost as before; Moby Dick (~1.3MB)
still completes well under 10 seconds

**Constraints**: Usage message and exit status must match the lesson exactly
on the missing-argument path; report output must be unchanged (from feature
007) on the happy path

**Scale/Scope**: One `main.py` update (import + argument handling)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Lesson Fidelity** — PASS. `sys.argv` usage, the `len(sys.argv) < 2`
  check, the exact usage message, and `sys.exit(1)` all match the lesson
  verbatim.
- **II. YAGNI / Course-Paced Simplicity** — PASS. No `argparse`, no flags,
  no optional arguments — just the single positional path the lesson asks
  for.
- **III. Standard Library Only** — PASS. `sys` is standard library; no
  third-party CLI framework.
- **IV. Incremental, Non-Destructive Growth** — PASS. `get_book_text`,
  `print_report`, and all of `stats.py` are unchanged; only how `main()`
  obtains the book path changes.
- **V. Readability Over Cleverness** — PASS. A simple `if`/`print`/`exit`
  guard at the top of `main()`, in the same style as the rest of the
  program.

No violations. Complexity Tracking table is not needed.

## Project Structure

### Documentation (this feature)

```text
specs/008-cli-arguments/
├── plan.md              # This file
├── quickstart.md         # Phase 1 output
└── tasks.md              # Phase 2 output (/speckit-tasks - not yet created)
```

research.md, data-model.md, and contracts/ are intentionally omitted: no
unresolved unknowns, no data entities, and the "interface" (command-line
argument) is fully described in spec.md's Functional Requirements.

### Source Code (repository root)

```text
main.py    # get_book_text(path), print_report(...), main() — now uses sys.argv[1]
stats.py   # unchanged
books/     # frankenstein.txt, mobydick.txt, prideandprejudice.txt (gitignored)
```

**Structure Decision**: No new files or layout changes — this feature only
modifies how `main()` obtains its book path.

## Complexity Tracking

*Not applicable — no constitution violations.*
