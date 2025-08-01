import sys
from stats import(
	get_word_count,
	get_char_count,
	sort_char
	)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    wordcount = get_word_count(text)
    characters = get_char_count(text)
    sorted_char = sort_char(characters)
    print_report(book_path, wordcount, sorted_char)

def print_report(book_path, wordcount, sorted_char):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for item in sorted_char:
        print(f"{item['char']}: {item['num']}")


main()
