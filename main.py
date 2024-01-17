def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(book):
    words = book.split()
    return len(words)

def get_char_count(book):
    letters = {}
    for char in book:
        char = char.lower()
        if char.isalpha():
            if char not in letters:
                letters[char] = 0
            letters[char] += 1
    return letters

def reverse_sort(letter_dict):
    new_dict = sorted(letter_dict.items(), key=lambda letter:letter[1], reverse=True)
    return dict(new_dict)

def create_report(sorted_dict, book_name, word_amount):
    print(f"--- Begin report for {book_name} ---")
    print(f"There are {word_amount} words in {book_name}\n")
    for letter in sorted_dict:
        print(f"The letter \"{letter}\" was found {sorted_dict[letter]} times")
    print("--- End of Report ---")

def main():
    book_path = "/home/justin/bootdev/localdevenv/books/frankenstein.txt"
    book_name = book_path.split("/")[-1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    #print(word_count)
    char_count = get_char_count(text)
    #print(char_count)
    sorted_decending_letters = reverse_sort(char_count)
    #print(sorted_decending_letters)
    create_report(sorted_decending_letters, book_name, word_count)

if __name__ == '__main__':
    main()