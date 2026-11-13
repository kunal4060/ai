# 8-Puzzle using BFS (graph: har board = node, har move = edge)
from collections import deque

start = ((3, 2, 1), (4, 0, 5), (7, 6, 8))
goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

def zero_pos(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def swap(state, i1, j1, i2, j2):
    grid = [list(row) for row in state]
    temp = grid[i1][j1]
    grid[i1][j1] = grid[i2][j2]
    grid[i2][j2] = temp
    return (tuple(grid[0]), tuple(grid[1]), tuple(grid[2]))

def neighbours(state):
    # 0 ke chaaron taraf ke moves = graph ke edges
    i, j = zero_pos(state)
    result = []
    if i > 0:
        result.append((swap(state, i, j, i - 1, j), 'U'))
    if i < 2:
        result.append((swap(state, i, j, i + 1, j), 'D'))
    if j > 0:
        result.append((swap(state, i, j, i, j - 1), 'L'))
    if j < 2:
        result.append((swap(state, i, j, i, j + 1), 'R'))
    return result

def bfs(start, goal):
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    parent = {start: None}
    move_used = {}
    while len(queue) > 0:
        current = queue.popleft()          # BFS: line me sabse aage wala
        if current == goal:
            break
        for nxt, mv in neighbours(current):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = current
                move_used[nxt] = mv
                queue.append(nxt)
    # goal se wapas start tak path jodo
    path = []
    moves = []
    node = goal
    while node is not None:
        path.append(node)
        if node in move_used:
            moves.append(move_used[node])
        node = parent[node]
    path.reverse()
    moves.reverse()
    return path, moves, len(visited)

path, moves, total_visited = bfs(start, goal)
print("Moves:", moves)
print("Number of moves:", len(moves))
print("States visited:", total_visited)
print("Start:")
for row in path[0]:
    print(row)
print("Goal:")
for row in path[len(path) - 1]:
    print(row)
