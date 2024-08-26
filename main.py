
def main():
    book_path = "books/frankenstein.txt"
    #text = get_book_text(book_path)
    #num_words = count_words(text)
    #print(f"{num_words} words found in the document")
    #print(count_chars(text))
    report(book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    lowered_string = text.lower()
    dict = {}
    for c in lowered_string:
        if c in dict:
            dict[c] = 1  + dict[c]
        else:
            dict[c] = 1 
    return dict

def report(book_path):
    text = get_book_text(book_path)
    num_words = count_words(text)

    dict = count_chars(text)
    char_arr = []
    for d in dict:
        if d.isalpha():
            char_arr.append( {"char":d,"num": dict[d]})

    def sort_on(dict):
        return dict["num"]

    char_arr.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for ch in char_arr:
        print(f"The '{ch['char']}' character was found {ch['num']} times")
    print("--- End report ---")
main()