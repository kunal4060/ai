"""DFS Module for 8-Puzzle — same problem, stack instead of queue."""
from collections import deque
from bfs_module import get_neighbors, show

START = (1, 2, 3, 0, 4, 6, 7, 5, 8)
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def dfs(start, goal, max_depth=30):
    """Depth-First Search using a STACK (list). LIFO -> go deep first!"""
    stack = [start]              # list as stack
    parent = {start: (None, '')}
    visited = {start}
    depth = {start: 0}
    while stack:
        cur = stack.pop()        # take from BACK (LIFO) <- only change!
        if cur == goal:
            break
        if depth[cur] >= max_depth:
            continue
        for nxt, mv in get_neighbors(cur):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = (cur, mv)
                depth[nxt] = depth[cur] + 1
                stack.append(nxt)
    path, moves, s = [], [], goal
    while s is not None:
        path.append(s)
        s, m = parent[s]
        moves.append(m)
    path.reverse()
    moves.reverse()
    return path, moves[1:], len(visited)


if __name__ == '__main__':
    path, moves, explored = dfs(START, GOAL)
    print(f"DFS -> Moves: {len(moves)} | Explored: {explored} states")
    print("Sequence:", ' -> '.join(moves), "\n")
    for i, st in enumerate(path):
        print(f"--- Step {i} ---")
        show(st)
