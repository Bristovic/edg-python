# simple program to count frequency of letters in text file
from os import strerror

print("Welcome to the character frequency counter.")
src_name = input("Please, enter the name of the text file to read: ")

try:
    src = open(src_name, "rt")
except IOError as e:
    print("Cannot open file: ", strerror(e.errno))
    exit(e.errno)

try:
    dest = open((src_name.replace(".txt", ".hist")), "wt")
except IOError as e:
    print("Cannot write new file: ", strerror(e.errno))
    exit(e.errno)

try:
    char_dict = {}
    char = src.read(1).lower()
    while char != "":
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
        char = src.read(1).lower()
    # using lambda to sort
    ordered_chars = sorted(char_dict,
                           key=lambda x: (char_dict[x], x),
                           reverse=True)
    print(ordered_chars)
    for key in ordered_chars:
        print(key, "->", char_dict[key])
        dest.write(key + " -> " + str(char_dict[key]) + "\n")
    dest.close()

except IOError as e:
    print("Unable to read and count file: ", strerror(e.errno))
    exit(e.errno)
