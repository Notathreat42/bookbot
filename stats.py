

def word_count(words):
    return len(words.split())

def char_counter(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char]+=1
        else:char_count[char] = 1
    return char_count


def dict_to_list(char_dict): 
    char_list = []
    def sort_on(my_dict):
        return my_dict["num"]
    for key, value in char_dict.items():
        char_list.append({"char": key, "num": value})
    char_list.sort(reverse=True, key =sort_on)
    return char_list


     

    
