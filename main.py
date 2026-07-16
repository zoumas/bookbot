from stats import get_num_words, get_num_chars, chars_dict_to_sorted_list


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_chars = chars_dict_to_sorted_list(num_chars)
    print(f"Found {num_words} total words")
    print(sorted_chars)


main()
