from os import strerror


class StudentDataException(Exception):
    pass


class BadLine(StudentDataException):
    def __init__(self, message="Bad line encountered:"):
        Exception.__init__(self, message)


class FileEmpty(StudentDataException):
    def __init__(self, message="Empty file encountered:"):
        Exception.__init__(self, message)


print("Welcome to the student grade evaluator.")
src_name = input("Please, enter the name of the text file to read: ")

try:
    src = open(src_name, "rt")
except IOError as e:
    print("Cannot open file:", src_name + ".", strerror(e.errno))
    exit(e.errno)

try:
    stud_dict = {}
    line = src.readline()
    if line == "":
        raise FileEmpty
    else:
        while line != "":
            student = line.split()[0] + " " + line.split()[1]
            if len(line.split()) != 3 or not student.isalpha():
                raise BadLine
            elif student in stud_dict:
                stud_dict[student] += float(line.split()[2])
            else:
                stud_dict[student] = float(line.split()[2])
            line = src.readline()
        ordered_studs = dict(sorted(stud_dict.items()))
        for key in ordered_studs:
            print(key, "->", stud_dict[key])
except FileEmpty as e:
    print(e, src_name)
    src.close()
    exit()
except BadLine as e:
    print(e, line)
    src.close()
    exit()
