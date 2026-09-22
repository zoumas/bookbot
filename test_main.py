import pytest

from main import count_words


@pytest.mark.parametrize(
    ("text", "want"),
    [
        ("", 0),
        ("    \n\t    \n\t", 0),
        ("Books are fun", 3),
        ("  leading and trailing  ", 3),
        ("line one\r\nline two\r\n", 4),
        ("tabs\tand\nnewlines", 3),
    ],
)
def test_count_words(text: str, want: int) -> None:
    assert count_words(text) == want
