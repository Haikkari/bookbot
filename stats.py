def count_words(filepath):
    """
    Reads the content of a book from a file and returns it's word count as an integer.
    
    :param filepath: Path to the book file.
    :return: Word count of the book as an integer.
    """
    with open(filepath) as file:
        book = file.read()
        words = book.split()
        return len(words)
    
def count_characters(filepath):
    """
    Reads the content of a book from a file and returns it's character count as a dictionary.
    
    :param filepath: Path to the book file.
    :return: Character count of the book as an dictionary.
    """
    with open(filepath) as file:
        book = file.read()
        character_list = list(book.lower())
        character_dict = {}
        for character in character_list:
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1
        return character_dict