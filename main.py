from stats import count_characters, character_report, count_words
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_file = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
        return file_contents
    
import sys
from stats import count_characters, character_report

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return f"Found {len(words)} total words"

import sys
from stats import count_characters, character_report

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return f"Found {len(words)} total words"

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")

    text = get_book_text(path_to_file)

    print("----------- Word Count ----------")
    print(count_words(text))

    print("--------- Character Count -------")
    characters = count_characters(text)
    sorted_chars = character_report(characters)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()



