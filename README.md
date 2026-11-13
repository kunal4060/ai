# AI Lab — CSE3002 Artificial Intelligence (VIT-AP)

All 10 lab experiments for the **AI Lab FAT** (Sat 14 Nov 2026, 8:00–9:40 AM, CB228).
Code in Python. FAT marking: Experiment writeup 15 + Code 10 + Execution/Demo 15 + Quiz 10 = 50.

## Experiments

| # | Experiment | File | Verified output |
|---|-----------|------|-----------------|
| 1 | 8-Puzzle (3×3) using BFS | `exp01_8puzzle_bfs.py` | 22 moves (optimal), 1,12,307 states visited |
| 2 | 8-Puzzle (3×3) using DFS | `exp02_8puzzle_dfs.py` | 30 moves (depth limit 30), 44,643 states visited |
| 3 | Shortest path using A* | `exp03_astar_shortest_path.py` | Distances from A on Graph 1 (weight 1) |
| 4 | Shortest path using Dijkstra | `exp04_dijkstra_shortest_path.py` | Same distances; A→L = 4 via A-B-C-H-L |
| 5 | Tic-Tac-Toe, User vs Computer (Random) | `exp05_tictactoe_random.py` | Interactive game |
| 6 | Tic-Tac-Toe, User vs Computer (Minimax) | `exp06_tictactoe_minimax.py` | Interactive game, computer never loses |
| 7 | Tic-Tac-Toe, User vs User | `exp07_tictactoe_user_vs_user.py` | Interactive game |
| 8 | 8-Queens problem | `exp08_8queens.py` | 92 solutions (backtracking) |
| 9 | Water Jug (4L + 3L → 1L) | `exp09_water_jug.py` | 2 steps: Fill 4L → Pour 4→3 = (1, 3) |
| 10 | Map Colouring (Graph 1) | `exp10_map_colouring.py` | Valid 3-colouring, verified |

## How to run

```bash
python3 exp01_8puzzle_bfs.py
python3 exp03_astar_shortest_path.py
python3 exp08_8queens.py
# ...any experiment the same way
```

Tic-Tac-Toe games (Exp 5, 6, 7) are interactive — enter row and column (0, 1 or 2) when asked.

## Notes

- **Exp 1 & 2** use the FAT start state `{{3,2,1},{4,0,5},{7,6,8}}` and goal `{{1,2,3},{4,5,6},{7,8,0}}`.
- **Exp 3, 4 & 10** use **Graph 1** from the FAT exam, edge weight = 1 for all edges.
  A* uses h(n) = 0 (admissible with no coordinates given), so it behaves like
  Uniform Cost Search and matches Dijkstra's distances.
- **Exp 9:** BFS finds the *shortest* solution — 2 steps. The textbook 8-step
  sequence also works, but BFS proves 2 steps is optimal.
- `extras/` has simpler teaching versions (BFS/DFS modules) and a Prolog
  vacuum-cleaner program from the lab.

## Author

Kunal Ugale (25BCE7607) — B.Tech CSE, VIT-AP.
