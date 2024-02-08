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
        count = sum(row)
        if count != 45:
            print("This sudoku is invalid. Check row", (table.index(row) + 1))
            return

    # check col sum
    for i in range(len(table)):
        count = 0
        for j in range(len(table[i])):
            count += table[j][i]
        if count != 45:
            print("This sudoku is invalid. Check column", (i + 1))
            return

    # check squares sum
    counts = 0
    for r in range(0, (len(table) - 2), 3):
        for c in range(0, (len(table) - 2), 3):
            count = 0
            for row in range(r, r+3):
                for col in range(c, c+3):
                    count += table[row][col]
            counts += 1
            if count != 45:
                print("This sudoku is invalid. Check square", counts)
                return

    # success
    return print("Check complete. This sudoku is valid.")


sudoku_checker()
