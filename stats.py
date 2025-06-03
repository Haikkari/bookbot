def count_words(filepath):
    with open(filepath) as file:
        book = file.read()
        words = book.split()
        return len(words)