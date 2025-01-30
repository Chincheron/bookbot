def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
#    print(file_contents)
    return file_contents

def word_count(string):
    words = string.split()
    #print(words)
    print(len(words))

main()

word_count(main())

