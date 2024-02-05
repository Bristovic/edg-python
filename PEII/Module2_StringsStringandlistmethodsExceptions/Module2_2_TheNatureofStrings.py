
# string is an immutable sequence of characters
word = "by"
print(len(word))  # 2

# exit character doesn't count
i_am = 'I\'m'
print(i_am)
print(len(i_am))  # 3 as backslash not counted

# multi-line strings require 3 apostrophes, 3 quotes
multiline_string = """This is
a string."""

print(len(multiline_string))  # remember invisible chars count (\n here)

# limited string operations
str_1 = "a"
str_2 = "b"

print(str_1 + str_2)  # concatenation, not commutative
print(str_2 + str_1)
print(5 * "a")  # replication

# the ord() function. gives ASCII/UNICODE code point value
char_1 = "a"
char_2 = " "  # space

print(ord(char_1))
print(ord(char_2))
print(ord("α"))  # greek alpha
print(ord("ę"))  # polish e

# operations on strings: chr()
print(chr(945))
print(chr(281))
print(chr(978))

# indexing strings
string_to_use = "what is the word?"

for char in range(len(string_to_use)):
    print(string_to_use[char], end=" ")  # can use index for char

print()

# can also iterate through strings. works the same.
for i in string_to_use:
    print(i, end=" ")

# can also use slices
print(string_to_use[1:4])
print(string_to_use[:4])
print(string_to_use[-5:])
print(string_to_use[-9:-6])

# using in or not in
print("the" in string_to_use)
print("?" in string_to_use)
print("!" in string_to_use)
print("!" not in string_to_use)
print("beans" not in string_to_use)
print("sentence" not in string_to_use)
print("hat" in string_to_use)  # watch out, will also pick out substrings
print(" hat" in string_to_use)  # putting space will do

# operations on strings
# del, append(), insert() not possibly. but + is
new_string = "Hey, " + string_to_use
print(new_string)

# min()
print(min("aAbByYzZ"))  # returns A. Why? Because A is lower code point.

t = "The Knights Who Say 'Ni!'"
print("[" + min(t) + "]")

u = [-1, 0, 1, 2]
print(min(u))

# max()
print(max("WwXxYyZz"))  # returns z. Why? Z is highest code point.

sequence = [0, 1, 2, 3, 4, 5, 6]
print(max(sequence))

# the index() method
print("aAbBcC".index("a"))
print("0123456789".index("9"))
print("123456789".index("9"))

# the list() function
print(list("123456789"))
print(list("Each character is a list element."))

# the count() method
print("abcdabcdabcd".count("b"))
print("abcdabcdabcd".count("e"))
