import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

from stats import get_num_words, get_num_characters, sort_char_counts

def main():
    with open(path) as f:
        text = f.read()

    word_count = get_num_words(text)
    character_count = get_num_characters(text)
    sorted_items = sort_char_counts(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("------------ Word Count ------------")
    print(f"Found {word_count} total words")
    print("------------ Character Count ------------")
    for item in sorted_items:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
        else:
            pass

    print("============ END ============")

if __name__ == "__main__":
    main()

