from collections.abc import Callable
from pathlib import Path

import pytest

from main import format_report, main


def test_format_report() -> None:
    got = format_report("books/x.txt", 3, [(" ", 5), ("e", 2), ("!", 1), ("t", 1)])
    want = (
        "============ BOOKBOT ============\n"
        "Analyzing book found at books/x.txt...\n"
        "----------- Word Count ----------\n"
        "Found 3 total words\n"
        "--------- Character Count -------\n"
        "e: 2\n"
        "t: 1\n"
        "============= END ==============="
    )
    assert got == want


@pytest.mark.parametrize(
    "argv",
    [
        pytest.param(["main.py"], id="no-args"),
        pytest.param(["main.py", "a.txt", "b.txt"], id="extra-args"),
    ],
)
def test_main_usage(argv: list[str], capsys: pytest.CaptureFixture[str]) -> None:
    assert main(argv) == 1
    assert capsys.readouterr().out == "Usage: python3 main.py <path_to_book>\n"


def test_main_report(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    book = tmp_path / "book.txt"
    book.write_text("Boot boot!", encoding="utf-8")

    assert main(["main.py", str(book)]) == 0
    out = capsys.readouterr().out
    assert "Found 2 total words\n" in out
    assert "o: 4\nb: 2\nt: 2\n" in out


@pytest.mark.parametrize(
    ("setup", "want_err"),
    [
        pytest.param(lambda path: None, "No such file or directory", id="missing"),
        pytest.param(lambda path: path.mkdir(), "Is a directory", id="directory"),
        pytest.param(
            lambda path: path.write_bytes(b"caf\xe9"),
            "not valid UTF-8 text",
            id="not-utf8",
        ),
    ],
)
def test_main_unreadable_book(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    setup: Callable[[Path], object],
    want_err: str,
) -> None:
    path = tmp_path / "book"
    setup(path)

    assert main(["main.py", str(path)]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == f"bookbot: {path}: {want_err}\n"
