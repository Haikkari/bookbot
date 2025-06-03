def get_book_text(filepath):
    """
    Reads the content of a book from a file and returns it as a string.
    
    :param filepath: Path to the book file.
    :return: Content of the book as a string.
    """
    with open(filepath) as file:
        return file.read()

def count_words(filepath):
    with open(filepath) as file:
        book = file.read()
        words = book.split()
        return len(words)
    
def main():
    # bookpath is a relative path to book and program prints the book on terminal
    bookpath = "books/frankenstein.txt"
    # print(get_book_text(bookpath))
    print(f"{count_words(bookpath)} words found in the document")

main()