import os


search_for = input("What file should I analyze?\n")

if search_for not in os.listdir('.'):
    print("Sorry, that doesn't seem to be a valid file.")
    quit()

char_dict = {}
word_dict = {}  # In "Hello, World!" the words are "Hello," and "World!"
num_lines = 0

with open(search_for, 'r') as file_object:
    content = file_object.read()
    for char in content:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    print(char_dict)

    words_array = content.split()
    for word in words_array:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    print(word_dict)

    num_lines = content.count("\n") + 1
    print("Line Count: " + str(num_lines))
