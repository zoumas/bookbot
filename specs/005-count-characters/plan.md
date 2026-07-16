# Implementation Plan: Count Characters

**Branch**: `005-count-characters` | **Date**: 2026-07-17 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/005-count-characters/spec.md`

## Summary

Add `get_num_chars(text) -> dict[str, int]` to `stats.py`, iterating over
`text.lower()` and tallying each character. Update `main.py` to import it,
call it on the loaded book text, and print the resulting dictionary after the
existing word-count line.

## Technical Context

**Language/Version**: Python 3 (3.14.6 locally)

**Primary Dependencies**: None (standard library `dict`, `str.lower()`)

**Storage**: N/A (operates on the in-memory string from `get_book_text`)

**Testing**: None introduced by this feature; correctness is verified by
`bootdev run <id>` / `bootdev run <id> -s` and manual `python3 main.py`.

**Target Platform**: Local developer machine (Linux/macOS/WSL2), CPython 3

**Project Type**: Two-file script (`main.py`, `stats.py`)

**Performance Goals**: N/A — single pass over a ~430KB string, well under 5
seconds

**Constraints**: Output mapping MUST be case-insensitive (one lowercase key
per character); no filtering of non-letter characters

**Scale/Scope**: One new function in `stats.py`, one `main()` update

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Lesson Fidelity** — PASS. Return type `dict[str, int]`, lowercase
  normalization via `.lower()`, and printing both the word count and the
  character mapping all match the lesson verbatim.
- **II. YAGNI / Course-Paced Simplicity** — PASS. A plain loop building a
  `dict` is the simplest approach; no `collections.Counter`, no sorting, no
  filtering — none of that is asked for yet.
- **III. Standard Library Only** — PASS. Uses only builtins (`dict`,
  `str.lower()`); `collections.Counter` is available in the standard library
  too but is deliberately not used, to keep the implementation as plain and
  readable as a beginner-lesson example (a manual loop mirrors how the
  course teaches this concept).
- **IV. Incremental, Non-Destructive Growth** — PASS. Builds on `stats.py`
  and `main.py` from feature 004; `get_num_words`/`get_book_text` are
  unchanged.
- **V. Readability Over Cleverness** — PASS. A straightforward `for`-loop
  with a `dict.get(..., 0) + 1` pattern is explicit and easy to follow.

No violations. Complexity Tracking table is not needed.

## Project Structure

### Documentation (this feature)

```text
specs/005-count-characters/
├── plan.md              # This file
├── quickstart.md         # Phase 1 output
└── tasks.md              # Phase 2 output (/speckit-tasks - not yet created)
```

research.md, data-model.md, and contracts/ are intentionally omitted: no
unresolved unknowns; the "entity" (character frequency mapping) is fully
described in spec.md's Key Entities; no external interface/contract beyond
console output.

### Source Code (repository root)

```text
main.py    # get_book_text(path), main() — imports get_num_words, get_num_chars from stats
stats.py   # get_num_words(text), get_num_chars(text)
```

**Structure Decision**: Continue with the two flat files established in
feature 004. `get_num_chars` joins `get_num_words` in `stats.py`, matching
the lesson's placement instruction.

## Complexity Tracking

*Not applicable — no constitution violations.*
