import os


search_for = input("What file should I analyze?\n")

if search_for not in os.listdir('.'):
    print("Sorry, that doesn't seem to be a valid file.")
    quit()

# Include the FULL path to the file; include r/w/
char_dict = {}
word_dict = {}
num_lines = 0

with open(search_for, 'r') as file_object:
    content = file_object.read()
    for char in content:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    print(char_dict)

    num_lines = len(file_object.readlines())
    print(num_lines)
""""
import os

files = os.listdir(".")
print(files)

files2 = os.scandir(".")
for file in files2:
    if (file.is_file()):
        print(file.name)
"""

"""
import glob

file_path = "**\\*.py"
files_list = glob.glob(file_path, recursive=True)
print(files_list)
"""
