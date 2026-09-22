from stats import count_characters, count_words, sort_by_count


def main() -> None:
    text = get_book_text("./books/frankenstein.txt")
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    char_counts = sort_by_count(count_characters(text))
    print(char_counts)


def get_book_text(filepath: str) -> str:
    with open(filepath, encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    main()
