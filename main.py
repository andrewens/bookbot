# private
def get_word_count(string):
    return len(string.split())


def count_each_char(string):
    char_count = dict()

    for char in string:
        char = char.lower()

        if char not in char_count:
            char_count[char] = 1
            continue
        
        char_count[char] += 1

    return char_count


# public
def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(count_each_char(file_contents))


main()
