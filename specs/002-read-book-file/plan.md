# Implementation Plan: Read Book File

**Branch**: `002-read-book-file` | **Date**: 2026-07-17 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/002-read-book-file/spec.md`

## Summary

Modify `main.py` to add `get_book_text(path)`, which opens a file at `path`
using a `with` block and returns its full contents as a string, and update
`main()` to call `get_book_text("books/frankenstein.txt")` and print the
result. This replaces the previous `print("greetings boots")` body of
`main()`.

## Technical Context

**Language/Version**: Python 3 (3.14.6 locally)

**Primary Dependencies**: None (standard library `open`/`with` only)

**Storage**: Local filesystem — reads `books/frankenstein.txt` (plain text
file, not tracked in git, fetched by an earlier lesson)

**Testing**: None introduced by this feature; correctness is verified by
`bootdev run <id>` / `bootdev run <id> -s` and manual `python3 main.py`.

**Target Platform**: Local developer machine (Linux/macOS/WSL2), CPython 3

**Project Type**: Single-file script

**Performance Goals**: N/A (one file read + one print, well under 5 seconds
for a ~430KB text file)

**Constraints**: Output must be the file's exact, complete contents — no
truncation, no added/removed whitespace beyond what's in the file itself

**Scale/Scope**: One file (`main.py`), two functions (`get_book_text`, `main`)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Lesson Fidelity** — PASS. Function names `get_book_text` and `main`,
  the `with open(path) as f: ... f.read()` pattern, and the path
  `books/frankenstein.txt` all match the lesson verbatim.
- **II. YAGNI / Course-Paced Simplicity** — PASS. No error handling, no
  encoding parameters, no CLI arguments — just what the lesson asks for.
- **III. Standard Library Only** — PASS. Uses only the `open` builtin and a
  `with` block.
- **IV. Incremental, Non-Destructive Growth** — PASS. Builds on the existing
  `main.py` from feature 001; only the body of `main()` changes, and
  `get_book_text` is new.
- **V. Readability Over Cleverness** — PASS. Two small, plainly-named
  functions; no clever one-liners.

No violations. Complexity Tracking table is not needed.

## Project Structure

### Documentation (this feature)

```text
specs/002-read-book-file/
├── plan.md              # This file
├── quickstart.md         # Phase 1 output
└── tasks.md              # Phase 2 output (/speckit-tasks - not yet created)
```

research.md, data-model.md, and contracts/ are intentionally omitted: no
unresolved unknowns, no persisted/structured data entities beyond "a string
of book text," and no external interface/contract beyond "run the script,
read stdout."

### Source Code (repository root)

```text
main.py    # get_book_text(path) + main(), main() invoked at module run time
```

**Structure Decision**: Continue with the single-file script at the
repository root established in feature 001. No `src/` layout is warranted yet
— the course hasn't introduced anything requiring one, and adding structure
ahead of need would violate YAGNI.

## Complexity Tracking

*Not applicable — no constitution violations.*
