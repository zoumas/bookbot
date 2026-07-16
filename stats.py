def get_num_words(text):
    return len(text.split())


def get_num_chars(text):
    char_counts = {}
    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts


def sort_on(pair):
    return pair[1]


def chars_dict_to_sorted_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append((char, count))
    return sorted(char_list, key=sort_on, reverse=True)
