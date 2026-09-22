def main() -> None:
    contents = get_book_text("./books/frankenstein.txt")
    print(contents)


def get_book_text(filepath: str) -> str:
    with open(filepath, encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    main()
