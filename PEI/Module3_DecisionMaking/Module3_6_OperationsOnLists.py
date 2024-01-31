
# reference semantics
list_1 = [1]
list_2 = list_1  # Copies memory location, not values.
list_1[0] = 2
print(list_2)  # Will output 2 because complex var names point to memory.

# does not apply if totally reassign variable
# changes both
x = [1, 2]
y = x
x[0] = 12
print(x, y)
y[0] = 36
print(x, y)

# changes neither
x = [1, 2]
y = x
x[0] = 12
print(x, y)
y[0] = 36
print(x, y)

# slice function
# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]  # second arg is up to but not inclusive index
print(new_list)
new_list = my_list[0:5]  # 1st to 5th element
print(new_list)

# to copy can also use method
list_2 = list_1.copy()

# negative indices
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-3:-1]  # take 3rd last and 2nd last elements.
print(new_list)

# omitting numbers on either side assumes from first or last
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:-1]  # first to penultimate.
print(new_list)
print(my_list)

# can also delete slices, but not a copy
del my_list[-2:]
print(my_list)

# deleting full slice will delete contents. deleting list deletes var.

# in and not in
in_list = [0, 25, 42, 12, -1]
print(5 in in_list)  # False
print(-1 in in_list)  # True
print(25 in in_list)  # True

# simple programs w/ lists
my_list = [12, 3, 11, 31, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i
print(largest)

# another program to find presence of number and location
asc_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in asc_list:
    found = asc_list[i] == to_find
    if found:
        break

if found:
    print("Element found at position", i+1)
else:
    print("Element not present")

# Assignment: removing repetitions
rep_lst = [0, 2, 3, 92, 1, 4, 32, 92, 0]
new_list = []
for i in rep_lst:
    if i in new_list:
        continue
    else:
        new_list.append(i)
rep_lst = new_list
print(rep_lst)

my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)
# AH! It increments every time. So the value is always the same.
