def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    import sys
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit([1])
    else:

    #print(get_book_text("books/frankenstein.txt"))
        wordcount = count_words(get_book_text(sys.argv[1]))
    #print(f"{wordcount} words found in the document")
        charcount = count_chars(get_book_text(sys.argv[1]))
    #print(f"Character Dictionary: {charcount}")
        sorted = sort_chars(get_book_text(sys.argv[1]))
        print('============ BOOKBOT ============')
        print(f'Analyzing book found at {sys.argv[1]}...')
        print('----------- Word Count ----------')
        print(f'Found {wordcount} total words')
        print('--------- Character Count -------')
        for char in sorted:
            if char['char'].isalpha():
                print(f'{char['char']}: {char['num']}')
        print('============= END ===============')

from stats import count_words
from stats import count_chars
from stats import sort_chars


main()
