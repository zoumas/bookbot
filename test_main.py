import pytest

from main import count_words


@pytest.mark.parametrize(
    ("text", "want"),
    [
        pytest.param("", 0, id="empty"),
        pytest.param("    \n\t    \n\t", 0, id="whitespace only"),
        pytest.param("Books are fun", 3, id="three words"),
        pytest.param(
            "  leading and trailing  ", 3, id="leading and trailing whitespace"
        ),
        pytest.param("line one\r\nline two\r\n", 4, id="carriage return and newline"),
        pytest.param("tabs\tand\nnewlines", 3, id="tab and newline"),
    ],
)
def test_count_words(text: str, want: int) -> None:
    assert count_words(text) == want
