# a basic example of a Python module

__counter = 0  # count for checking no. of func. calls.


# func def for summing list
def sum_list(inp_list):  # takes one arg: input list
    global __counter  # makes scope global to add invoc to counter
    __counter += 1  # adds to (global) counter each invoc
    list_sum = 0  # inits sum of list as 0
    for i in inp_list:  # for each element in input list
        list_sum += i  # add the element to
    return list_sum



if __name__ == "__main__":
    print("I am running independently.")
else:
    print("I am running as an imported module.")
