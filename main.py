def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    #print(get_book_text("books/frankenstein.txt"))
    wordcount = count_words(get_book_text("books/frankenstein.txt"))
    #print(f"{wordcount} words found in the document")
    charcount = count_chars(get_book_text("books/frankenstein.txt"))
    #print(f"Character Dictionary: {charcount}")
    sorted = sort_chars(get_book_text("books/frankenstein.txt"))
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
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
