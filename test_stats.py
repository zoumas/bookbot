import pytest

from stats import count_characters, count_words


@pytest.mark.parametrize(
    ("text", "want"),
    [
        pytest.param("", 0, id="empty"),
        pytest.param("    \n\t    \n\t", 0, id="whitespace-only"),
        pytest.param("Books are fun", 3, id="three-words"),
        pytest.param("  leading and trailing  ", 3, id="surrounding-whitespace"),
        pytest.param("line one\r\nline two\r\n", 4, id="crlf"),
        pytest.param("tabs\tand\nnewlines", 3, id="tab-and-newline"),
    ],
)
def test_count_words(text: str, want: int) -> None:
    assert count_words(text) == want


@pytest.mark.parametrize(
    ("text", "want"),
    [
        pytest.param("", {}, id="empty"),
        pytest.param("Boot!", {"b": 1, "o": 2, "t": 1, "!": 1}, id="lesson-example"),
        pytest.param("AaA", {"a": 3}, id="case-folding"),
        pytest.param("\na b\n", {"a": 1, " ": 1, "b": 1, "\n": 2}, id="whitespace"),
        pytest.param("Éé", {"é": 2}, id="non-ascii"),
    ],
)
def test_count_characters(text: str, want: dict[str, int]) -> None:
    assert count_characters(text) == want
