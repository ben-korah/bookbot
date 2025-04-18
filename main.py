def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    #print(get_book_text("books/frankenstein.txt"))
    wordcount = count_words(get_book_text("books/frankenstein.txt"))
    print(f"{wordcount} words found in the document")

from stats import count_words

main()
