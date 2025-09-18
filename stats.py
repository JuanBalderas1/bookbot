# A file that contains functions for analyzing the text.

def get_num_words(text: str) -> int:
    return len(text.split())

def get_num_characters(text: str) -> dict[str, int]:
    lower_case_string = text.lower()
    letter_counts: dict[str, int] = {}
    for ch in lower_case_string:
        letter_counts[ch] = letter_counts.get(ch, 0) + 1
    return letter_counts

def sort_char_counts(counts: dict[str, int]) -> list[dict[str, int]]:
    items: list[dict[str, int]] = []
    for ch, n in counts.items():
        items.append({"char": ch, "num":n})
    items.sort(key=lambda item: item["num"], reverse=True)
    return items
