"""BFS Module for 8-Puzzle — clean, reusable, exam-ready."""
from collections import deque


def get_neighbors(state):
    """All states reachable by one blank-tile move. Returns [(new_state, move)]."""
    s = list(state)
    i = s.index(0)
    r, c = divmod(i, 3)
    out = []
    for dr, dc, mv in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            ns = s.copy()
            ns[i], ns[j] = ns[j], ns[i]
            out.append((tuple(ns), mv))
    return out


def bfs(start, goal):
    """Breadth-First Search. Returns (path, moves, states_explored)."""
    queue = deque([start])
    parent = {start: (None, '')}
    visited = {start}
    while queue:
        cur = queue.popleft()
        if cur == goal:
            break
        for nxt, mv in get_neighbors(cur):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = (cur, mv)
                queue.append(nxt)
    path, moves, s = [], [], goal
    while s is not None:
        path.append(s)
        s, m = parent[s]
        moves.append(m)
    path.reverse()
    moves.reverse()
    return path, moves[1:], len(visited)


def show(state):
    for r in range(3):
        print(' '.join(str(x) if x else '_' for x in state[r*3:(r+1)*3]))
    print()


if __name__ == '__main__':
    START = (1, 2, 3, 0, 4, 6, 7, 5, 8)
    GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    path, moves, explored = bfs(START, GOAL)
    print(f"Moves: {len(moves)} | Explored: {explored} states")
    print("Sequence:", ' -> '.join(moves), "\n")
    for i, st in enumerate(path):
        print(f"--- Step {i} ---")
        show(st)
