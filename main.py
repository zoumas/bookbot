import sys

from stats import get_num_words, get_num_chars, chars_dict_to_sorted_list


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, sorted_char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("---------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_char_list:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_chars = chars_dict_to_sorted_list(num_chars)
    print_report(book_path, num_words, sorted_chars)


main()
