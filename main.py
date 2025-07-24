from stats import *

def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
        return contents

def print_report(num_words, character_list, filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in character_list:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

def main():
    filepath = "books/frankenstein.txt"
    contents = get_book_text(filepath)
    num_words = get_number_wordcount(contents)
    character_count = get_character_count(contents)
    list_of_dicts = []

    for char, count in character_count.items():
        # Create a new dictionary for each character
        new_dict = {"char": char, "num": count}
        list_of_dicts.append(new_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)

    print_report(num_words, list_of_dicts, filepath)

main()