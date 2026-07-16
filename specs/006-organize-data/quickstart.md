# Quickstart: Organize Data

## Prerequisites

- Python 3 installed (`python3 --version`)
- `books/frankenstein.txt` present at the project root

## Run

```bash
python3 main.py
```

## Expected Outcome

Console prints, in order:

1. `Found 75767 total words`
2. A list of `(character, count)` tuples ordered from most to least
   frequent, e.g. `[(' ', 70480), ('e', 44538), ('t', 29493), ...]`

No raw, unordered dictionary is printed.

## Validation

- Manual: run the command above; confirm the list's counts are
  non-increasing from left to right.
- Automated: `bootdev run <lesson-id>` (and `-s` to submit) against this
  lesson's check.
