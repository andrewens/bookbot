# const
CHARS_TO_COUNT = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

# private
def get_word_count(string):
    return len(string.split())


def count_each_char(string):
    char_count = dict()

    for char in string:
        char = char.lower()

        if char not in CHARS_TO_COUNT:
            continue

        if char not in char_count:
            char_count[char] = 1
            continue
        
        char_count[char] += 1

    return char_count


def dict_to_sorted_tuples_array(dictionary):
    array = []

    for key, value in dictionary.items():
        array.append((key, value))

    array.sort(reverse=True, key=lambda tuple : tuple[1])

    return array


def print_book_report(book_path):
    file_contents = ""
    with open(book_path) as f:
        file_contents = f.read()

    word_count = get_word_count(file_contents)
    char_count = count_each_char(file_contents)
    char_count = dict_to_sorted_tuples_array(char_count)

    print("--- Begin report of " + book_path + " ---")
    print(str(word_count) + " words found in the document")
    print()
    
    for char_tuple in char_count:
        print(f"The '{char_tuple[0]}' character was found {char_tuple[1]} times")

    print()
    print("--- End report ---")


# public
def main():
    print_book_report("books/frankenstein.txt")


main()
