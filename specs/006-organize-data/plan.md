# Implementation Plan: Organize Data

**Branch**: `006-organize-data` | **Date**: 2026-07-17 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/006-organize-data/spec.md`

## Summary

Add `sort_on(pair)` and `chars_dict_to_sorted_list(char_dict)` to `stats.py`.
`sort_on` returns `pair[1]` (the count) for use as a sort key.
`chars_dict_to_sorted_list` builds a list of `(char, count)` tuples from the
dict and returns `sorted(list, key=sort_on, reverse=True)`. Update `main.py`
to convert the character-count dict via this function and print the sorted
list instead of the raw dict.

## Technical Context

**Language/Version**: Python 3 (3.14.6 locally)

**Primary Dependencies**: None (standard library `sorted()`)

**Storage**: N/A (operates on the in-memory dict from `get_num_chars`)

**Testing**: None introduced by this feature; correctness is verified by
`bootdev run <id>` / `bootdev run <id> -s` and manual `python3 main.py`.

**Target Platform**: Local developer machine (Linux/macOS/WSL2), CPython 3

**Project Type**: Two-file script (`main.py`, `stats.py`)

**Performance Goals**: N/A — single sort over ~60-100 dict entries (distinct
characters), negligible cost

**Constraints**: Output list must be strictly non-increasing by count; raw
dict no longer printed

**Scale/Scope**: Two new functions in `stats.py`, one `main()` update

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Lesson Fidelity** — PASS. Function names `sort_on` and
  `chars_dict_to_sorted_list`, the `(char, count)` tuple order, and the
  `sorted(..., key=sort_on, reverse=True)` call all match the lesson
  verbatim.
- **II. YAGNI / Course-Paced Simplicity** — PASS. No custom sort algorithm,
  no dataclasses — a plain tuple list and the builtin `sorted()`.
- **III. Standard Library Only** — PASS. Uses only `sorted()` and a plain
  `list`.
- **IV. Incremental, Non-Destructive Growth** — PASS. Builds on
  `get_num_chars` from feature 005; that function is unchanged.
- **V. Readability Over Cleverness** — PASS. `sort_on` as a named helper
  (rather than an inline `lambda`) matches the lesson's own teaching
  example and keeps the sort key self-documenting.

No violations. Complexity Tracking table is not needed.

**Note on an interpretive assumption (flagged for user review)**: The spec's
Assumptions section records a judgment call — that the raw character-count
dict is no longer printed once the sorted list exists, rather than printing
both. This wasn't explicit in the lesson extraction. If the lesson actually
expects both to be printed, this is a one-line change in `main.py` to make
after implementation.

## Project Structure

### Documentation (this feature)

```text
specs/006-organize-data/
├── plan.md              # This file
├── quickstart.md         # Phase 1 output
└── tasks.md              # Phase 2 output (/speckit-tasks - not yet created)
```

research.md, data-model.md, and contracts/ are intentionally omitted: no
unresolved unknowns beyond the flagged assumption above; the "entity"
(ordered list) is fully described in spec.md; no external interface/contract
beyond console output.

### Source Code (repository root)

```text
main.py    # get_book_text(path), main() — imports get_num_words, get_num_chars, chars_dict_to_sorted_list from stats
stats.py   # get_num_words(text), get_num_chars(text), sort_on(pair), chars_dict_to_sorted_list(char_dict)
```

**Structure Decision**: Continue with the two flat files established in
feature 004/005. Both new functions join `stats.py`, matching the lesson's
placement instruction.

## Complexity Tracking

*Not applicable — no constitution violations.*
