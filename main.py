def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Bergin report of {book_path} ---")
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document")
    chars_dict = get_char_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    chars_list = []
    for char in chars_sorted_list:
        print(f"The '{char['char']}' character was found {char['count']} times")
    print("--- End report ---")


def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    chars = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char not in chars:
                chars[char] = 0
            chars[char] += 1
    return chars

def sort_on(dict):
    return dict["count"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "count": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()