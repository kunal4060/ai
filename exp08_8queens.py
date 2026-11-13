# Exp 8 - 8-Queens problem (backtracking)
# 8x8 chess board pe 8 queens aise rakho ki koi bhi queen dusri ko
# attack na kare: same row, same column, ya same diagonal me 2 queens
# nahi honi chahiye. Backtracking se saare solutions nikalte hain.
# Kul 92 solutions hote hain (12 fundamental + rotations/reflections).

def is_safe(board, row, col):
    # upar wali rows me check karo (neeche abhi queens rakhi nahi)
    for i in range(row):
        # same column?
        if board[i] == col:
            return False
        # diagonal? (row ka farak == column ka farak)
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve(row, board, solutions):
    if row == 8:  # saari 8 queens rakh di - solution mil gaya!
        solutions.append(board.copy())
        return
    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col  # queen rakho
            solve(row + 1, board, solutions)  # agli row pe jao
            board[row] = -1  # BACKTRACK - queen hatao, wapas jao


def show(board):
    for r in range(8):
        line = ""
        for c in range(8):
            line += "Q " if board[r] == c else ". "
        print(line)
    print()


if __name__ == '__main__':
    solutions = []
    solve(0, [-1] * 8, solutions)
    print("Total solutions:", len(solutions))
    print("\nPehla solution (row -> column):", solutions[0])
    print("\nBoard:")
    show(solutions[0])
