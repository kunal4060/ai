# Exp 5 - Tic-Tac-Toe: User (X) vs Computer (O) - Random approach
# Computer har baari khaali dabbon me se RANDOM ek dabba chunta hai.
# Koi strategy nahi - isiliye user aaram se jeet sakta hai.

import random


def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print()


def check_winner(board):
    # 3 rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
    # 3 columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != " ":
            return board[0][j]
    # 2 diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None


def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def computer_move(board):
    # khaali dabbe nikalo, unme se RANDOM ek chuno
    empty = [(i, j) for i in range(3) for j in range(3)
             if board[i][j] == " "]
    return random.choice(empty)


# ---------------- game shuru ----------------
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print("Tic-Tac-Toe: Tum X ho, Computer O hai (Random moves)")
print("Row aur Column 0, 1 ya 2 me do")
print_board(board)

while True:
    r = int(input("Row (0-2): "))
    c = int(input("Col (0-2): "))
    if board[r][c] != " ":
        print("Ye dabba bhara hai, dobara try karo")
        continue
    board[r][c] = "X"
    print_board(board)
    if check_winner(board) == "X":
        print("Tum jeet gaye!")
        break
    if is_full(board):
        print("Draw ho gaya!")
        break
    print("Computer random move khel raha hai...")
    m = computer_move(board)
    board[m[0]][m[1]] = "O"
    print_board(board)
    if check_winner(board) == "O":
        print("Computer jeet gaya! (lucky random move)")
        break
    if is_full(board):
        print("Draw ho gaya!")
        break
