# Tic-Tac-Toe project
import random


def display_board(brd_stat):
    print("+---+---+---+\n"
        "¦", brd_stat[0][0], "¦", brd_stat[0][1], "¦", brd_stat[0][2], "¦\n"
        "+---+---+---+\n"
        "¦", brd_stat[1][0], "¦", brd_stat[1][1], "¦", brd_stat[1][2], "¦\n"
        "+---+---+---+\n"
        "¦", brd_stat[2][0], "¦", brd_stat[2][1], "¦", brd_stat[2][2], "¦\n"
        "+---+---+---+\n")
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def make_list_of_free_fields(brd_stat):
    free_fields = []
    for row in range(3):
        for square in range(3):
            if brd_stat[row][square] in range(1, 10):
                free_fields.append(brd_stat[row][square])
    return free_fields
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    # I changed this just to read the numbers. woops


def victory_for(brd_stat):
    victory = "ongoing"
    for index in range(3):
        if (brd_stat[index][0]
                == brd_stat[index][1]
                == brd_stat[index][2]):
            victory = "win"
            break
        elif (brd_stat[0][index]
              == brd_stat[1][index]
              == brd_stat[2][index]):
            victory = "win"
            break
        else:
            continue
    if brd_stat[0][0] == brd_stat[1][1] == brd_stat[2][2]:
        victory = "win"
    elif brd_stat[0][2] == brd_stat[1][1] == brd_stat[2][0]:
        victory = "win"
    elif victory != "win" and not make_list_of_free_fields(brd_stat):
        victory = "draw"

    return victory
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game


def enter_move(brd_stat):
    global sgn
    sgn = "0"
    while True:
        move = int(input("Enter your move (1-9): "))
        if move in make_list_of_free_fields(brd_stat):
            break
        else:
            continue
    for row in range(3):
        for square in range(3):
            if brd_stat[row][square] == move:
                brd_stat[row][square] = sgn
    display_board(brd_stat)
    return victory_for(brd_stat)
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.


def draw_move(brd_stat):
    global sgn
    sgn = "X"
    print("My turn!")
    while True:
        move = random.randint(1, 9)
        if move in make_list_of_free_fields(brd_stat):
            break
        else:
            continue
    for row in range(3):
        for square in range(3):
            if brd_stat[row][square] == move:
                brd_stat[row][square] = sgn
    display_board(brd_stat)
    return victory_for(brd_stat)
    # The function draws the computer's move and updates the board.


def tictactoe():
    vic = "ongoing"
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    display_board(board)
    print("I'll go first.")
    board[1][1] = "X"
    display_board(board)
    while vic == "ongoing":
        vic = enter_move(board)
        if vic != "ongoing":
            break
        vic = draw_move(board)
    if vic == "win":
        print(sgn, "wins!")
    elif vic == "draw":
        print("It's a draw!")


def play_again():
    while True:
        play = input("Would you like to play a game of TicTacToe? y/n")
        if play == "y":
            tictactoe()
        elif play == "n":
            print("Goodbye!")
            exit()
        else:
            continue


play_again()


