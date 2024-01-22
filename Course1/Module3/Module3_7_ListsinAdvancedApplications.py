# Lists of lists
row = []
for i in range(8):
    row.append(WHITE_PAWN)

# makes a row of pawns as in a chessboard
empty = "0"
rook = "R"
pawn = "p"
board = [[empty for square in range(8)] for row in range(8)]

# print the board, row by row
for row in board:
    print(row)

# set the board with rooks
board[0][0] = rook
board[0][7] = rook
board[7][0] = rook
board[7][7] = rook

# place pawns
board[1] = [pawn for square in range(8)]
board[6] = [pawn for square in range(8)]

for row in board:
    print(row)

# hourly temp readings by month table
# empty table of 24*31 to give hours per day in a month
temps = [[0.0 for h in range(24)] for d in range(31)]
# some data enters here then:

# to find average noon temperature in a month
total = 0.0
for day in temps:  # day is a list of with 24 hourly temps
    total += day[11]
avg_temp = total / 31  # assume 31 days a month

# booking for a 3 building, 15 floor, 20 room hotel
# makes all rooms (20) on each floor (15) for each building (3) empty
rooms = [[[False for r in range(20)] for f in range(15) for t in range(3)]]

# to book one out, enter building, room, floor
rooms[0][9][13] = True  # building 2, 10th floor, room 14: occupied

# to check for vacancies in 15th floor of 3rd building
vacancy = 0
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

# 2d array
table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'

# 3d array

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'
