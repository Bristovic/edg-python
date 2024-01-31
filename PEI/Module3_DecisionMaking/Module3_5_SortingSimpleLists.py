
# Bubble sort example
sort_list = [8, 10, 6, 2, 4]  # List to sort
swapped = True

while swapped:
    swapped = False
    for i in range(len(sort_list) - 1):  # len-1 is number of pairs
        if sort_list[i] > sort_list[i+1]:
            swapped = True
            sort_list[i], sort_list[i+1] = sort_list[i+1], sort_list[i]
print(sort_list)  # Obviously v inefficient.

# Advanced version
my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

# But Python has its own in-built.
sort_list = [8, 10, 6, 2, 4]
print(sort_list)
sort_list.sort()
print(sort_list)
