from stats import get_num_words
from stats import count_words
from stats import sort_dic
import sys

arguments = sys.argv[1:]
if len(arguments) < 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    for book in arguments:
        text = get_book_text(book)
        num_words = get_num_words(text)
        print(f"Found {num_words} total words")
        new_dict = (count_words(text))
        sorted_dict = sort_dic(new_dict)
        for item in sorted_dict:
            if  item.isalpha() == True:
                print(f"{item}: {sorted_dict[item]}")
            else:
                pass





def get_book_text(path):
    with open(path) as f:
        return f.read()



main()