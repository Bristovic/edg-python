# onto the lists
numbers = [10, 5, 7, 2, 1]
print(numbers)
numbers[0] = 111  # Assign value 111 to first element (index 0).
print(numbers)

numbers[1] = numbers[4]  # Change element 2 to value of element 5
print(numbers)

print(numbers)  # Access whole list.
print(numbers[0])  # Access a list element on its own.

# The len function
print(f"The list is {len(numbers)} elements long.")

# Removing elements
del numbers[1]  # This will change indexes for all subsequent elements.
print(len(numbers))
print(numbers)

# Cannot access elements that don't exist. numbers[4] now doesn't refer.
# Negative indices are illegal. So can use for other things.

# Negative indices index in descending order.
print(numbers[-1])  # Will print last element (1 in this case)
print(numbers[-2])  # Will print penultimate element (2 in this case)

# Assignment: rabbit-hat list
numbers = [1, 2, 3, 4, 5]
replace = int(input("Enter a whole number to replace in the list."))
numbers[2] = replace  # Replace third element with chosen number.

del numbers[-1]  # Delete last element
print(len(numbers))

# Optimised
numbers = [1, 2, 3, 4, 5]
numbers[2] = int(input("Enter a whole number to replace in the list."))
del numbers[-1]
print(len(numbers))

# Methods and method invocation
# Appending
list_test = [1, "a", 99, "Albert", 3.56]
print(list_test)

list_test.append(111)  # Adds data to end of list. it is a method.
print(list_test)

# Inserting. A more precise method. index then value
list_test.insert(2, "insertion")
print(list_test)

# Initiating an empty list
new_list = []

print(f"The list contains: {new_list}.")
for i in range(5):
    new_list.append(i + 1)
    print(f"The list contains: {new_list}.")

new_list = []
print(f"The list contains: {new_list}.")
for i in range(5):
    new_list.insert(0, i + 1)
    print(f"The list contains: {new_list}.")

# Using for. Very effective with lists.
num_list = [10, 22, 3, -4, 5]

# Iterating through index elements and then adding element to total.
total = 0
for i in range(len(num_list)):
    total += num_list[i]
print(total)

# Can do this more simply (as I did originally, fuck)
total = 0
for i in num_list:
    total += i
print(total)

# Lists in action. Reordering.
# Say wanted to reassign elements.
var_1 = 1
var_2 = 2
print(var_1, var_2)

# Allows reassignment without losing variable.
var_1, var_2 = var_2, var_1
print(var_1, var_2)

# Applies also to lists
num_list = [10, 22, 3, -4, 5]
print(num_list)
num_list[0], num_list[4] = num_list[4], num_list[0]
print(num_list)

# Using for in longer list. Clunky way of reversing
num_list = [10, 22, 3, -4, 5]
print(num_list)
for i in range(len(num_list)//2):
    num_list[i], num_list[len(num_list) - i - 1] = num_list[len(num_list) - i - 1], num_list[i]
print(num_list)

# Assignment: Beatles list
beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(beatles)

for i in range(2):
    beatles.append(input("Add a member (Stu Sutcliffe or Pete Best):"))
print(beatles)

del beatles[-1]
del beatles[-1]
beatles.insert(0, "Ringo Starr")
print(beatles)
