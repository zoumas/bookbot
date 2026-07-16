# Quickstart: Count Characters

## Prerequisites

- Python 3 installed (`python3 --version`)
- `books/frankenstein.txt` present at the project root

## Run

```bash
python3 main.py
```

## Expected Outcome

Console prints two things, in order:

1. `Found 75767 total words`
2. A dictionary mapping lowercase characters to their counts, e.g.
   `{'﻿the': ...}` — actual output is a Python `dict` literal like
   `{'t': 12345, 'h': 6789, ...}`.

## Validation

- Manual: run the command above; spot-check a common letter's count (e.g.
  `'e'`) looks plausible for the book's length (~430KB of English text).
  Confirm mixed-case letters aren't split (no separate `'T'` and `'t'` keys).
- Automated: `bootdev run <lesson-id>` (and `-s` to submit) against this
  lesson's check.
