# program to check validity of a sudoku-table
def sudoku_checker():
    str_table = input("Enter a list of 9 sudoku rows, separated by spaces: ").split()
    table = []

    # make to columns
    for row in str_table:
        table.append(list(row))

    # convert to digits
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = int(table[i][j])

    # check row sum
    for row in table:
        count = 0
        count = sum(row)
        if count != 45:
            print("This sudoku is invalid.")
            return

    # check col sum
    for i in range(len(table)):
        count = 0
        for j in range(len(table[i])):
            count += table[i][j]
        if count != 45:
            print("This sudoku is invalid.")
            return

    # check squares sum
    for i in

    count = 0


    print(table)

if sum(table[row]) == 45:
    success

if sum(table[row])

sudoku_checker()
