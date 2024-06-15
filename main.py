PATH_TO_FILE = "books/frankenstein.txt"

def main():
    book_text = get_book_text(PATH_TO_FILE)
    word_count = get_word_count(book_text)
    dict_word_count = get_char_count(book_text)
    #getting list of char dicts for sorting
    list_of_dicts = rebuild_dict(dict_word_count)
    list_of_dicts.sort(reverse=True, key=sort_on)
    
    #Creating a report
    print(f'--- Begin report of {PATH_TO_FILE}')
    print(f'{word_count} words in the document\n')
    for char_dict in list_of_dicts:
        print(f"The '{char_dict['name']}' character was found {char_dict['num']} times")
    print('--- End report ---')

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    dict_char_count = {}
    for char in set(text.lower()):
        dict_char_count[char] = text.lower().count(char)
    return dict_char_count

def sort_on(dict):
    return dict["num"]

def rebuild_dict(dict):
    list_of_dict = []
    for char in dict:
        enhanced_dict = {}
        if char.isalpha():
            enhanced_dict = {
                "name": char,
                "num": int(dict[char])
            }
            list_of_dict.append(enhanced_dict)
    return list_of_dict







main()