from stats import count_characters, count_words, sort_by_count


def main() -> None:
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = count_words(text)
    char_counts = sort_by_count(count_characters(text))
    report = format_report(filepath, num_words, char_counts)
    print(report)


def get_book_text(filepath: str) -> str:
    with open(filepath, encoding="utf-8") as f:
        return f.read()


def format_report(
    filepath: str, num_words: int, char_counts: list[tuple[str, int]]
) -> str:
    lines = [
        "============ BOOKBOT ============",
        f"Analyzing book found at {filepath}...",
        "----------- Word Count ----------",
        f"Found {num_words} total words",
        "--------- Character Count -------",
    ]
    for char, count in char_counts:
        if not char.isalpha():
            continue
        lines.append(f"{char}: {count}")
    lines.append("============= END ===============")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
