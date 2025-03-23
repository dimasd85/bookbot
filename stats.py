def get_num_words(file_content):
    lines = file_content.split()
    num_words = len(lines)
    # print(f"{num_words} words found in the document")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

def get_num_char(file_content):
    char_counts = {}
    for char in file_content:
        char = char.lower()
        if char in char_counts:
            char_counts[char] +=1
        else:
            char_counts[char] = 1
        
    return char_counts

def sort_dict_char(dict_char):
    char_list = []
    for char, count in dict_char.items():
        char_dict = {"char": char, "count": count}
        char_list.append(char_dict)

    def sort_on(dict_item):
        return dict_item["count"]
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list