# Exp 7 - Tic-Tac-Toe: User vs User (2 players, 3x3 grid)
# Player 1 = X, Player 2 = O. Baari-baari se row/col daalo.
# Jo pehle 3 apne ek line me kar le, wo jeetta hai.

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


# ---------------- game shuru ----------------
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print("Tic-Tac-Toe: Player 1 = X, Player 2 = O")
print("Row aur Column 0, 1 ya 2 me do")
print_board(board)

current = "X"  # pehli baari X ki
while True:
    print(f"Player {current} ki baari:")
    r = int(input("Row (0-2): "))
    c = int(input("Col (0-2): "))
    if board[r][c] != " ":
        print("Ye dabba bhara hai, dobara try karo")
        continue
    board[r][c] = current
    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"Player {winner} jeet gaya!")
        break
    if is_full(board):
        print("Draw ho gaya!")
        break
    # baari badlo: X -> O, O -> X
    current = "O" if current == "X" else "X"
