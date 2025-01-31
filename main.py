def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
#    print(file_contents)
    return file_contents

def word_count(string):
    words = string.split()
    #print(words)
    return(len(words))

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
    #print(character_counts)
    return character_counts

def print_report():
    character_counts = character_count(text)
    character_list = []
    for i in character_counts:
        if i.isalpha():
            character_list.append(i)
    alpha_counts = {}
    for character in character_list:
         alpha_counts[character] = character_counts[character]
    alpha_counts = sorted(alpha_counts.items(), key=lambda x: x[1], reverse=True)
    #print(alpha_counts)
    
    #print report output
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(text)} words found in the document\n")
    
    for letter, count in alpha_counts:
        print(f"The letter '{letter}' occurs {count}  times.")
    print ("--- End report ---")
    

text = main()

print_report()
