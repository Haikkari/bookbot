from stats import count_words, count_characters, sorted_character_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    bookpath = sys.argv[1]
    sorted_list = sorted_character_list(count_characters(bookpath))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(bookpath)} total words")
    print("--------- Character Count -------")

    for character in sorted_list:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")

    print("============= END ===============")

main()