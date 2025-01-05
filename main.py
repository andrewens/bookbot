
def get_word_count(string):
    return len(string.split())


def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        # print(file_contents)
        print(get_word_count(file_contents))


main()
