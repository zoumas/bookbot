from stats import count_characters, count_words


def main() -> None:
    text = get_book_text("./books/frankenstein.txt")
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    char_counts = count_characters(text)
    print(f"Character count: {char_counts}")


def get_book_text(filepath: str) -> str:
    with open(filepath, encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    main()
