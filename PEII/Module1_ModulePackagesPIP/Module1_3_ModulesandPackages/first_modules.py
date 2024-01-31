# basic Python module

"""first_modules.py - a basic Python module to explore functionality and
containing two functions for import: 'sum_list()' and 'prod_list().
"""

# line for helping Unix and Unix-like OSs run the file
#!/usr/bin/env python3

# count for checking no. of func. calls.
__counter = 0


# func def for summing list
def sum_list(inp_list): # takes one arg: input list
    global __counter  # makes scope global to add invoc to counter
    __counter += 1  # adds to (global) counter each invoc
    list_sum = 0  # inits sum of list as 0
    for i in inp_list:  # for each element in input list
        list_sum += i  # add the element to
    print("Inside:", __counter)
    return list_sum


# func def for finding product of all list elements
def prod_list(inp_list):
    global __counter
    __counter += 1
    list_prod = 1
    for i in inp_list:
        list_prod *= i
    print("Inside:", __counter)
    return list_prod


# place for testing func functionality
if __name__ == "__main__":
    print("I am running independently. \nRunning tests.")

    # function test data. list of ints 1-5
    test_list = [i + 1 for i in range(5)]

    # test for summing. return True
    print(sum_list(test_list) == 15)

    # test for multiplying. return True
    print(prod_list(test_list) == 120)
