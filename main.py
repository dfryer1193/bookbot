from stats import count_words, count_chars, sorted_by_char_counts

def get_book_text(fpath):
    with open(fpath, 'r') as f:
        return f.read()

def main():
    text = get_book_text('books/frankenstein.txt')
    num_words = count_words(text)
    char_count = count_chars(text)
    sorted = sorted_by_char_counts(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in sorted:
        print(f"{d['char']}: {d['count']}")

    print("============= END ===============")

main()
