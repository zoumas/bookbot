from main import format_report


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
