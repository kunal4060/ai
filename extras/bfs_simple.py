"""8-Puzzle BFS - SUPER SIMPLE version. Sirf if/for/while!"""
from collections import deque


# 0 (khaali) kis number pe hai?
def find_zero(state):
    for i in range(9):
        if state[i] == 0:
            return i


# khaali ke padosi states banao
def get_neighbors(state):
    s = list(state)
    i = find_zero(s)
    r = i // 3      # row (// matlab bhaag, dashamlav hata do)
    c = i % 3       # col (% matlab remainder)
    result = []
    moves = [[-1, 0, 'U'], [1, 0, 'D'], [0, -1, 'L'], [0, 1, 'R']]
    for m in moves:
        nr = r + m[0]
        nc = c + m[1]
        # grid ke andar hai?
        if nr >= 0 and nr < 3 and nc >= 0 and nc < 3:
            j = nr * 3 + nc
            ns = s[:]            # copy banao
            temp = ns[i]         # swap karo
            ns[i] = ns[j]
            ns[j] = temp
            result.append([tuple(ns), m[2]])
    return result


def bfs(start, goal):
    queue = deque()
    queue.append(start)          # line me pehla = start
    parent = {}                  # roti ke tukde: main kahan se aaya
    parent[start] = None
    move_taken = {}              # kaunsi move se aaya
    move_taken[start] = ''
    visited = [start]            # dekhe hue states ki list

    while len(queue) > 0:
        cur = queue.popleft()    # line ke AAGE se nikaalo
        if cur == goal:          # manzil mil gayi?
            break
        neighbors = get_neighbors(cur)
        for pair in neighbors:
            nxt = pair[0]
            mv = pair[1]
            if nxt not in visited:   # naya hai?
                visited.append(nxt)
                parent[nxt] = cur
                move_taken[nxt] = mv
                queue.append(nxt)    # line ke PEECHE lagao

    # rasta nikalo - goal se start tak ULTA chalo
    path = []
    moves = []
    s = goal
    while s is not None:
        path.append(s)
        moves.append(move_taken[s])
        s = parent[s]
    path.reverse()
    moves.reverse()
    return path, moves[1:]


# board sundar print karo
def show(state):
    for r in range(3):
        line = ""
        for c in range(3):
            x = state[r * 3 + c]
            if x == 0:
                line = line + "_ "
            else:
                line = line + str(x) + " "
        print(line)
    print("")


start = (1, 2, 3, 0, 4, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

path, moves = bfs(start, goal)
print("Total moves:", len(moves))
print("Moves:", moves)
print("")
for i in range(len(path)):
    print("Step", i)
    show(path[i])
