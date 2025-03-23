import sys
import os
from stats import get_num_words 
from stats import get_num_char
from stats import sort_dict_char

def get_book_text(path_to_file):
    with open(path_to_file, "r", encoding='utf-8') as f:
        file_contents = f.read()        
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>", flush=True)
        sys.exit(1)

    book_path = sys.argv[1]

    # to read the input file and store the contenu in a variable
    # and call a function to print how many words are in the document 
    text = get_book_text(book_path)
    get_num_words(text)

    # call the function, to create a dictionary with the counts for each character found in the text
    char_dict = get_num_char(text)    

    # to sort the dictionary of chars and their counts in descending order, accrordingly to thei count (from max to least)
    sorted_list = sort_dict_char(char_dict)   

    print("--------- Character Count -------")
    for item in sorted_list:
        char = item['char']
        count = item['count']
        if char.isalpha():
            print(f"{char}: {count}")


# This should be at the end of the file, outside any function
if __name__ == "__main__":
    main()