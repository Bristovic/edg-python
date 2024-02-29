# Module on processing files
from os import strerror

# Opening testtext.txt in read mode,
# Returning it as a file object.
text_stream = open("testtext.txt", "rt", encoding="utf-8")

# Printing the contents of the file to the console.
print(text_stream.read())

# More complex reading and handling
try:
    count = 0
    comp_txt_stream = open("comp_text.txt", "rt")
    comp_text_chars = comp_txt_stream.read(1)
    while comp_text_chars != "":
        print(comp_text_chars, end="")
        count += 1
        comp_text_chars = comp_txt_stream.read(1)
    comp_txt_stream.close()
    print("\n\nCharacters in file:", count)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# Simple code for reading, but beware memory limitations!
try:
    cnt = 0
    s = open('comp_text.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


# Reading text file as lines, not characters.
try:
    ccount = lcount = 0
    c_txt_strm = open("comp_text.txt", "rt")
    c_line = c_txt_strm.readline()
    while c_line != "":
        lcount += 1
        for ch in c_line:
            print(ch, end="")
            ccount += 1
        c_line = c_txt_strm.readline()
    c_txt_strm.close()
    print("\n\nCharacters in file:", ccount, end="")
    print("\n\nLines in file:", lcount)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# readlines
try:
    ccount = lcount = 0
    c_txt_strm = open("comp_text.txt", "rt")
    c_lines = c_txt_strm.readlines(20)
    while len(c_lines) != 0:
        for line in c_lines:
            lcount += 1
            for ch in line:
                print(ch, end="")
                ccount += 1
        c_lines = c_txt_strm.readlines(10)
    c_txt_strm.close()
    print("\n\nCharacters in file:", ccount, end="")
    print("\n\nLines in file:", lcount)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# Simplifying the code.
# the object from open() is an iterable
# does not need to be saved to handle
# it automatically invokes close() when the read reaches file end
# so:
try:
    chr_cnt = ln_cnt = 0
    for line in open("comp_text.txt", "rt"):
        ln_cnt += 1
        for char in line:
            print(char, end="")
            chr_cnt += 1
    print("\n\nCharacters in file:", chr_cnt)
    print("Lines in file:", ln_cnt)
except IOError as e:
    print(("I/O error occurred: ", strerror(e.errno)))


# writing to a file, printing (from new chars, not file)
try:
    # creates a new file (newtext.txt) to write to
    new_stream = open("newtext.txt", "wt")
    for i in range(10):
        line = "line #" + str(i+1) + "\n"
        for char in line:
            new_stream.write(char)
            print(char, end="")
    new_stream.close()
except IOError as e:
    print("I/O error occured:", strerror(e.errno))


# writing to a file line by line
try:
    # creates a new file (newtext.txt) to write to
    new_stream = open("newtext.txt", "wt")
    for i in range(10):
        new_stream.write("line by line # " + str(i+1) + "\n")

    new_stream.close()
except IOError as e:
    print("I/O error occured:", strerror(e.errno))

# bytearray introduction
# creates bytearray of size 10 bytes
data = bytearray(10)

# sets value for bytes as 10-1
for i in range(len(data)):
    data[i] = 10 - i

# prints the byte values in hexadecimal format
for b in data:
    print(hex(b))


# writing a bytearray to binary file
new_data = bytearray(10)

for i in range(len(data)):
    new_data[i] = ord("Z") - i

try:
    binary_file = open("new_binary.bin", "wb")
    binary_file.write(new_data)
    binary_file.close()
except IOError as e:
    print("I/O error:", strerror(e.errno))


# reading a byte array

# initialise new byte array to read into
read_data = bytearray(10)

try:
    # open binary file in read binary mode
    binary_file = open("new_binary.bin", "rb")
    # read it into new byte array
    binary_file.readinto(read_data)
    # close the stream
    binary_file.close()

    for b in read_data:
        print(hex(b), end="")
except IOError as e:
    print("I/O error:", strerror(e.errno))


# using read and the bytes class
try:
    bin_f = open("new_binary.bin", "rb")
    # use read to create bytes object
    # bytes object used to create bytearray
    read_data = bytearray(bin_f.read())
    print("\n")

    for b in read_data:
        print(hex(b), end="|")

except IOError as e:
    print("I/O error:", strerror(e.errno))


# using read with arg to specify byte maximum
try:
    bin_f = open("new_binary.bin", "rb")
    # use read to create bytes object
    # bytes object used to create bytearray
    read_data = bytearray(bin_f.read(5))
    print("\n")

    for b in read_data:
        print(chr(b), end="|")

except IOError as e:
    print("I/O error:", strerror(e.errno))
