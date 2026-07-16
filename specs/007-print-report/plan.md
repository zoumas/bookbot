# Implementation Plan: Print a Report

**Branch**: `007-print-report` | **Date**: 2026-07-17 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/007-print-report/spec.md`

## Summary

Add `print_report(book_path, num_words, sorted_char_list)` to `main.py`,
printing the exact report format specified by the lesson: opening header,
book path line, word-count section, alphabetical-only character-count
lines (filtered via `str.isalpha()`), and closing line. Update `main()` to
call this single function instead of its two separate `print()` calls.

## Technical Context

**Language/Version**: Python 3 (3.14.6 locally)

**Primary Dependencies**: None (standard library `print()`, `str.isalpha()`)

**Storage**: N/A (operates on in-memory values passed as parameters)

**Testing**: None introduced by this feature; correctness is verified by
`bootdev run <id>` / `bootdev run <id> -s` and manual `python3 main.py`,
comparing output line-by-line against the lesson's example.

**Target Platform**: Local developer machine (Linux/macOS/WSL2), CPython 3

**Project Type**: Two-file script (`main.py`, `stats.py`)

**Performance Goals**: N/A — a handful of `print()` calls plus one filtered
loop over ~60-100 tuples, negligible cost

**Constraints**: Report text (headers, section labels, closing line) must
match the lesson's example exactly, character for character

**Scale/Scope**: One new function in `main.py`, one `main()` update

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Lesson Fidelity** — PASS. Function name, parameters, and every line
  of report text are copied verbatim from the lesson's example, including
  the asymmetric dash counts in the character-count header.
- **II. YAGNI / Course-Paced Simplicity** — PASS. A straightforward function
  with a `for` loop and `if char.isalpha()` filter; no templating engine,
  no string-building abstraction beyond plain f-strings/print calls.
- **III. Standard Library Only** — PASS. Uses only `print()` and
  `str.isalpha()`.
- **IV. Incremental, Non-Destructive Growth** — PASS. Builds on `main.py`
  and `stats.py` from features 001-006; no existing function changes,
  only `main()`'s print calls are consolidated into one new function.
- **V. Readability Over Cleverness** — PASS. The report is built with plain,
  sequential `print()` statements in the same order as the required output
  — easy to compare line-by-line against the spec.

No violations. Complexity Tracking table is not needed.

## Project Structure

### Documentation (this feature)

```text
specs/007-print-report/
├── plan.md              # This file
├── quickstart.md         # Phase 1 output
└── tasks.md              # Phase 2 output (/speckit-tasks - not yet created)
```

research.md, data-model.md, and contracts/ are intentionally omitted: no
unresolved unknowns (the exact report text is fully specified), no data
entities beyond the report text itself, and no external interface/contract
beyond console output.

### Source Code (repository root)

```text
main.py    # get_book_text(path), print_report(book_path, num_words, sorted_char_list), main()
stats.py   # get_num_words(text), get_num_chars(text), sort_on(pair), chars_dict_to_sorted_list(char_dict) — unchanged
```

**Structure Decision**: `print_report` lives in `main.py` (not `stats.py`),
per the lesson's explicit placement — it's a presentation/output concern,
distinct from the data-computation functions in `stats.py`.

## Complexity Tracking

*Not applicable — no constitution violations.*
