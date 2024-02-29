# simple tool to copy the contents of a file
from os import strerror

source_name = input("Enter the file source name: ")
try:
    source = open(source_name, "rb")
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)

dest_name = input("Enter the file destination name: ")
try:
    dest = open(dest_name, "wb")
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    source.close()
    exit(e.errno)

buffer = bytearray(65536)
total = 0
try:
    read_in = source.readinto(buffer)
    while read_in > 0:
        written = dest.write(buffer[:read_in])
        total += written
        read_in = source.readinto(buffer)
except IOError as e:
    print("Cannot create write to destination file: ", strerror(e.errno))
    exit(e.errno)

print(total, "byte(s) successfully written")
source.close()
dest.close()
