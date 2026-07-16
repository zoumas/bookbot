# Quickstart: Read Book File

## Prerequisites

- Python 3 installed (`python3 --version`)
- `books/frankenstein.txt` present at the project root (fetched via the
  "Book Data" lesson's `curl` command)

## Run

```bash
python3 main.py
```

## Expected Outcome

Console prints the complete contents of `books/frankenstein.txt` — the full
novel text, unmodified — and nothing else. No trace of the earlier
"greetings boots" message.

## Validation

- Manual: run the command above; compare output length/start/end against
  `cat books/frankenstein.txt` to confirm it's the full, unmodified text.
- Automated: `bootdev run <lesson-id>` (and `-s` to submit) against this
  lesson's check.
