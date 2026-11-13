# Exp 3 - Shortest path distances from a source vertex using A* algorithm
# Graph 1 (FAT exam), edge weight = 1 for all edges, source = A
#
# A* = best-first search with f(n) = g(n) + h(n)
#   g(n) = cost from source to n (so far)
#   h(n) = heuristic estimate from n to goal
# Yahan graph me nodes ke coordinates nahi diye, isliye h(n) = 0 use kiya
# (admissible heuristic). h = 0 hone se A* Uniform Cost Search jaisa behave
# karta hai aur Dijkstra ke barabar shortest distances deta hai.

import heapq

# Graph 1 - adjacency list (FAT exam, page 3)
GRAPH_1 = {
    'A': ['B', 'F'],
    'B': ['A', 'C', 'F'],
    'C': ['B', 'F', 'G', 'H'],
    'D': ['H'],
    'E': ['F', 'I'],
    'F': ['A', 'B', 'C', 'E', 'G', 'I'],
    'G': ['C', 'F', 'J', 'K'],
    'H': ['C', 'D', 'L'],
    'I': ['E', 'F'],
    'J': ['G'],
    'K': ['G'],
    'L': ['H'],
}


def heuristic(node, goal):
    # No coordinates given in the exam graph, so h(n) = 0 (admissible).
    return 0


def astar(graph, source, goal=None):
    # g = source se ab tak ka cost, f = g + h
    g = {v: float('inf') for v in graph}
    g[source] = 0
    prev = {v: None for v in graph}
    pq = [(0 + heuristic(source, goal), 0, source)]  # (f, g, node)
    visited = set()
    order = []  # kis order me nodes settle hue
    while pq:
        f, cost, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        order.append(u)
        for v in graph[u]:  # har neighbour (weight = 1)
            if g[u] + 1 < g[v]:
                g[v] = g[u] + 1
                prev[v] = u
                heapq.heappush(pq, (g[v] + heuristic(v, goal), g[v], v))
    return g, prev, order


def reconstruct_path(prev, source, target):
    path, cur = [], target
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path if path and path[0] == source else []


if __name__ == '__main__':
    SOURCE = 'A'
    TARGET = 'L'
    dist, prev, order = astar(GRAPH_1, SOURCE, TARGET)
    print("Settle order:", ' -> '.join(order))
    print("\nShortest distances from", SOURCE, "(edge weight = 1):")
    for v in sorted(dist):
        print(f"  {SOURCE} -> {v} = {dist[v]}")
    path = reconstruct_path(prev, SOURCE, TARGET)
    print(f"\nShortest path {SOURCE} -> {TARGET}: {' -> '.join(path)} "
          f"(distance {dist[TARGET]})")
