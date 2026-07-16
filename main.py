def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    return len(text.split())


def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")


main()
