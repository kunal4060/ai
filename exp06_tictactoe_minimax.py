# Tic-Tac-Toe: User (X) vs Computer (O) - MiniMax algorithm
# MiniMax matlab: computer har move ke baad aage ka khel sochta hai,
# apne liye best score (jeet) aur user ke liye worst score dhoondhta hai.

def print_board(board):
    for i in range(3):
        row = ""
        for j in range(3):
            row = row + board[i][j] + " "
        print(row)
    print()

def check_winner(board):
    # 3 rows check karo
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
    # 3 columns check karo
    for j in range(3):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j] and board[0][j] != " ":
            return board[0][j]
    # 2 diagonals check karo
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def minimax(board, is_max):
    # is_max True = computer (O) ki baari, False = user (X) ki baari
    winner = check_winner(board)
    if winner == "O":
        return 1     # computer jeetega
    if winner == "X":
        return -1    # user jeetega
    if is_full(board):
        return 0     # draw
    if is_max:
        best = -10
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "   # move wapas lo (backtrack)
                    if score > best:
                        best = score
        return best
    else:
        best = 10
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "   # move wapas lo (backtrack)
                    if score < best:
                        best = score
        return best

def computer_move(board):
    best_score = -10
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# ---------------- game shuru ----------------
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print("Tic-Tac-Toe: Tum X ho, Computer O hai")
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
    print("Computer soch raha hai...")
    m = computer_move(board)
    board[m[0]][m[1]] = "O"
    print_board(board)
    if check_winner(board) == "O":
        print("Computer jeet gaya!")
        break
    if is_full(board):
        print("Draw ho gaya!")
        break
