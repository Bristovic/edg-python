# creating tuples (immutable sequence type). use brackets
tuple_1 = (1, 2, 3, 4)
tuple_2 = (1.0, 2.0, 3.0)

print(tuple_1, tuple_2)

# tuples may have mixed datatypes
tuple_mixed = (1, "b", 3.0)

print(tuple_mixed)

# creating empty tuple
empty_tuple = ()

# creating one-element tuple. requires a comma
one_element_tuple = (1,)

# accessing tuple elements list with index and slice
print(tuple_1[0])
print(tuple_1[-1])
print(tuple_mixed[1:])

# but they cannot be modified!
# using tuples
print(len(tuple_2))  # gives num of elements
print(tuple_1 + (1, 2))  # adds to tuple
print(tuple_2 * 2)  # multiplies tuple
print(5 in tuple_mixed)  # checks if val in tuple

# tuples on left side of assignment operator
t_var = 456

t1 = (1, )
t2 = (2, )
t3 = (3, t_var)  # a tuples elements can be variables

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

# tuple elements right of assignment can be expressions
t4 = (1, 2, 3 * 6, t_var * 2)

# dictionaries
# making a dictionary
dict_dan = {"cat": "kat", "dog": "hund", "horse": "hest"}
dict_num = {"me": 3234156565, "you": 9990192343}
empty_dict = {}

print(dict_dan, dict_num, empty_dict)  # prints whole dict

# using a dictionary
print(dict_dan["cat"])
print(dict_num["me"])
print(dict_dan["fish"])  # invalid key produces runtime error

# easy to avoid invalid keys using `in` and `not in`
words = ["cat", "fish", "horse"]
for word in words:
    if word in dict_dan:
        print(word, "is", dict_dan[word] + ".")
    else:
        print(word, "is not in the dictionary.")

# hanging indent for big expressions
dict_dan = {
            "zebra": "zebra",
            "cat": "kat",
            "dog": "hund",
            "horse": "hest"
            }

# using the `keys()` method to get a list of keys for iterating
for key in dict_dan.keys():
    print(key, "is", dict_dan[key] + ".")

# using `sorted()` to sort output
for key in sorted(dict_dan.keys()):
    print(key, "is", dict_dan[key] + ".")

# using `items()` method to get tuples of key-value pairs
for english, danish in dict_dan.items():
    print(danish, "is", english)

# using `values()` method to get values
for dan in sorted(dict_dan.values()):
    print(dan)

# modifying and adding values
# replacing a value by assigning to existing key
dict_dan["cat"] = "killing"

# adding a new key by assigning value to new key
dict_dan["swan"] = "svane"
print(dict_dan)


# updating dictionary with `update()` method
dict_dan.update({"duck": "and"})
print(dict_dan)

# removing a key (and value) with del keyword
del dict_dan["swan"]  # non-existent key will cause error

# removing last item using `popitem()` method
dict_dan.popitem()
print(dict_dan)


# using tuples and dictionaries together
# avg score program. my solution
print("This program calculates average score. "
      "When finished with data entry, enter "
      "empty name to see averages.")

school_class = {}
count = {}

while True:
    # take student name
    stud_name = input("Enter student name:")
    if stud_name == "":
        break
    # take student score
    stud_score = int(input("Enter student score (0-10:"))
    if stud_score < 0 or stud_score > 10:
        break
    # if student name already in dict of students
    if stud_name in school_class:
        # add score to value associated with name key
        school_class[stud_name] += stud_score
        # add one to total count of entered scores with name key
        count[stud_name] += 1
    # if new student name
    else:
        # add new key (their name) and assign first score to total score
        school_class[stud_name] = stud_score
        # add new key (their name) to count dict and 1 as scores entered
        count[stud_name] = 1

# once broken loop
# for each key in the school class (keys method)
for name in school_class.keys():
    # print the key name and average score is
    print(name + "'s average score is",
          # and provide the score by referring to total score
            # keyed to name in school class dict
            # and total count of scores, keyed to name in count dict
          (school_class[name]/count[name]))

# their solution
school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break

    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

# testing executing paths
temperature = float(input("Enter current temperature: "))


# four execution paths here
def temp_check(tempr):
    if tempr >= 100:
        print("You are boiling, literally.")
    elif tempr > 0:
        print("Above freezing.")
    elif tempr < 0:
        print("Below freezing.")
    else:
        print("It is literally freezing right now.")


# dataset to hit all execution paths
temps = [-20, -10_000, 10, 99, 123, 0]

# checking loop
for temp in temps:
    temp_check(temp)
