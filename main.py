import sys
def get_book_text(path):
    with open(path) as f:
        return f.read()
    

from stats import word_count
from stats import char_counter
from stats import dict_to_list  
    


def main():
   if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
   book_path = sys.argv[1]
   text = get_book_text(book_path)
   num_words = word_count(text)
   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {book_path}")
   print("----------- Word Count ----------")
   print(f"Found {num_words} total words")
   print("--------- Character Count -------")
   char_counts = char_counter(text)
   sorted_chars = dict_to_list(char_counts)
   for item in sorted_chars:
       if item["char"].isalpha():
       # Print as "e: 44538"
           print(f"{item['char']}: {item['num']}")
   print("============= END ==============")



main()
