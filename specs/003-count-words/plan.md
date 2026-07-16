# Implementation Plan: Count Words

**Branch**: `003-count-words` | **Date**: 2026-07-17 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/003-count-words/spec.md`

## Summary

Add `get_num_words(text)` to `main.py`, returning `len(text.split())`.
Update `main()` to call it on the text returned by `get_book_text`, and print
`f"Found {num_words} total words"` instead of printing the raw book text.

## Technical Context

**Language/Version**: Python 3 (3.14.6 locally)

**Primary Dependencies**: None (standard library `str.split()` / `len()`)

**Storage**: N/A (operates on the in-memory string from `get_book_text`)

**Testing**: None introduced by this feature; correctness is verified by
`bootdev run <id>` / `bootdev run <id> -s` and manual `python3 main.py`.

**Target Platform**: Local developer machine (Linux/macOS/WSL2), CPython 3

**Project Type**: Single-file script

**Performance Goals**: N/A (single `.split()` + `len()` over a ~430KB string,
well under 5 seconds)

**Constraints**: Output must be exactly one line, `Found {num_words} total
words`, with the correct integer count; no raw book text in the output

**Scale/Scope**: One file (`main.py`), one new function (`get_num_words`),
one `main()` update

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Lesson Fidelity** — PASS. Output format `Found {num_words} total
  words` matches the lesson verbatim. Function name `get_num_words` is a
  reasonable choice where the lesson explicitly allows naming flexibility
  (per spec Assumptions).
- **II. YAGNI / Course-Paced Simplicity** — PASS. `len(text.split())` is the
  simplest possible implementation; no manual tokenization or regex.
- **III. Standard Library Only** — PASS. Uses only `str.split()` and `len()`.
- **IV. Incremental, Non-Destructive Growth** — PASS. Builds on `main.py`
  from features 001/002; `get_book_text` is unchanged, only `main()`'s body
  and one new function are added.
- **V. Readability Over Cleverness** — PASS. `len(text.split())` is a
  standard, immediately readable Python idiom for word counting.

No violations. Complexity Tracking table is not needed.

## Project Structure

### Documentation (this feature)

```text
specs/003-count-words/
├── plan.md              # This file
├── quickstart.md         # Phase 1 output
└── tasks.md              # Phase 2 output (/speckit-tasks - not yet created)
```

research.md, data-model.md, and contracts/ are intentionally omitted: no
unresolved unknowns, the only "entity" is a plain integer count, and there's
no external interface/contract beyond "run the script, read stdout."

### Source Code (repository root)

```text
main.py    # get_book_text(path), get_num_words(text), main()
```

**Structure Decision**: Continue with the single-file script established in
features 001/002. Still no `src/` layout — three small functions in one file
remains simple enough that splitting would be premature structure.

## Complexity Tracking

*Not applicable — no constitution violations.*
