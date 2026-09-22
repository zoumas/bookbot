# bookbot

[![Python Version](https://img.shields.io/badge/python-3.14-3776AB?logo=python)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A command-line text analyzer. `bookbot` reads a plain text book, counts its
words, and prints how often each letter appears, from most to least common.

```text
$ python3 main.py books/frankenstein.txt
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
...
ô: 1
============= END ===============
```

## Features

- Word count, splitting on any run of whitespace (spaces, tabs, `\n`, `\r\n`).
- Case-insensitive letter frequencies, sorted from most to least common.
  Letters are Unicode-aware, so `æ` and `ê` are counted alongside `a`–`z`.
- Stable ordering: letters with equal counts keep their order of first
  appearance in the book.
- Unreadable books (missing, a directory, not UTF-8) are reported on stderr
  with exit code `1`, never with a traceback.
- No third-party runtime dependencies.

## Installation

```sh
git clone https://github.com/zoumas/bookbot
cd bookbot
```

Requires Python 3.14 or newer. BookBot uses only the standard library, so
there is nothing to install to run it.

## Usage

Books are not committed to the repository. Download the sample books first:

```sh
mkdir -p books
curl -L "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/frankenstein.txt" -o books/frankenstein.txt
curl -L "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/mobydick.txt" -o books/mobydick.txt
curl -L "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/prideandprejudice.txt" -o books/prideandprejudice.txt
```

Use these exact commands rather than copying the text by hand: the counts
depend on the files' exact contents.

Then pass the path of any plain text file:

```sh
python3 main.py books/frankenstein.txt
```

| Exit code | Meaning |
| --- | --- |
| `0` | The report was printed. |
| `1` | Wrong number of arguments (usage is printed), or the book could not be read. |

```text
$ python3 main.py
Usage: python3 main.py <path_to_book>
$ python3 main.py nope.txt
bookbot: nope.txt: No such file or directory
```

Books are decoded as UTF-8.

## Architecture

```text
main.py    entry point: arguments, file reading, error reporting, report formatting
stats.py   pure text analysis: word count, character counts, sorting
```

Notes on the design:

- **`stats.py` does no I/O.** Every function takes a string or a dict and
  returns a value, so each one is tested with plain inputs and no files.
- **`main.py` is the only place that touches the process.** `main` takes
  `argv` and returns an exit code; only the `__main__` guard reads `sys.argv`
  and calls `sys.exit`. Tests call `main([...])` directly.
- **The report is built, then printed.** `format_report` returns a string, so
  the exact output format is pinned by a golden test rather than by capturing
  stdout.
- **Errors are handled at the edge.** `get_book_text` lets `OSError` and
  `UnicodeDecodeError` propagate; `main` turns them into one-line messages on
  stderr. The usage message stays on stdout, which is what the course tests
  expect.

## Development

The project is managed with [uv](https://docs.astral.sh/uv/). `pytest` and
`ruff` are development dependencies.

```sh
uv sync                 # create .venv and install dev dependencies
uv run pytest           # run the tests
uv run ruff check       # lint
uv run ruff format      # format
```

Tests are table-driven with `pytest.mark.parametrize` and one named case per
row, use `tmp_path` for file fixtures and `capsys` for stdout and stderr.

## What this project is

`bookbot` was built as the guided project
[Build a BookBot in Python](https://www.boot.dev/courses/build-bookbot-python)
on [boot.dev](https://www.boot.dev/), then taken past the course requirements:
a uv-managed project with linting, formatting and tests, a testable entry
point, error handling without tracebacks, and a pure analysis module.

[![Boot.dev Build a BookBot in Python certificate](https://qvault-webapp-dynamic-assets.storage.googleapis.com/certificates/a17755e6-ff81-4991-b99c-6cefbbbdd3c4.jpeg?v=1790118605)](https://www.boot.dev/certificates/a17755e6-ff81-4991-b99c-6cefbbbdd3c4)

### What the project covers

**Local development setup.** Running Python from the terminal instead of a
browser editor, organizing projects in a workspace, and managing the project
with uv: a pinned Python version in `.python-version`, dev dependencies and a
committed `uv.lock`, so every machine gets the same tools.

**File I/O.** Reading a file with `open` in a `with` block, and always passing
`encoding="utf-8"`, because the default comes from the locale. Text mode turns
`\r\n` into `\n`, and one of the books starts with a UTF-8 byte order mark: the
kind of detail real data always has.

**Text processing.** `str.split()` with no argument versus `split(" ")`,
counting with a dict and `dict.get`, `str.lower()` versus `str.casefold()`,
and `str.isalpha()` being Unicode-aware. Sorting with `sorted`, a `key` of
`operator.itemgetter(1)`, and `reverse=True`, which keeps the sort stable.

**Formatted output.** Building the report as a list of lines joined once,
rather than with `+=`, and returning it instead of printing it.

**Command-line arguments.** Reading `sys.argv`, validating the argument count,
returning exit codes, and keeping errors off stdout so a report can be
redirected to a file cleanly.

**Designing for tests.** Splitting pure analysis from I/O, passing `argv` into
`main`, and testing every function in isolation: table-driven cases, golden
output, temporary files, and captured streams. Breaking the code on purpose,
for example `split(" ")` for `split()`, confirms the tests actually fail.

## License

[MIT](LICENSE).

## Credits

Book texts from [Project Gutenberg](https://www.gutenberg.org/), in the public
domain in the United States. This is an unofficial, non-commercial learning
project.
