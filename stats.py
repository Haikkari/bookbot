from main import get_book_text

def count_words(filepath):
    """
    Counts the words of a book from a file and returns it as an integer.
    
    :param filepath: Path to the book file.
    :return: Amount of words in a book as an integer.
    """
    book = get_book_text(filepath)
    words = book.split()
    return len(words)