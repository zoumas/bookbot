import operator


def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts


def sort_by_count(counts: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
