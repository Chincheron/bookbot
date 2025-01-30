def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
#    print(file_contents)
    return file_contents

def word_count(string):
    words = string.split()
    #print(words)
    print(len(words))

def character_count(string):
    #convert to lower case for comparison
    lower_string = string.lower()
   
    #iterate through each character and assign to dictionary   
    character_counts = {}
    for i in lower_string:
        if i in character_counts:
            character_counts[i] = character_counts[i] + 1
        else:
            character_counts[i] = 1
    print(character_counts)


text = main()

word_count(text)

character_count(text)

