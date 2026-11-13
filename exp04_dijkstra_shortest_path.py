# Exp 4 - Shortest path distances from a source vertex using Dijkstra's algorithm
# Graph 1 (FAT exam), edge weight = 1 for all edges, source = A
#
# Dijkstra = greedy best-first search. Har baar unsettled nodes me se
# sabse chhoti tentative distance wala node nikalo (uski distance final
# hoti hai - settled property), phir uske neighbours ko relax karo.
# Min-heap (priority queue) use hoti hai: O((V + E) log V).

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


def dijkstra(graph, source):
    dist = {v: float('inf') for v in graph}
    prev = {v: None for v in graph}
    dist[source] = 0
    visited = set()
    pq = [(0, source)]  # min-heap of (distance, node)
    order = []  # kis order me nodes settle hue
    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:  # purani heap entry - skip karo
            continue
        visited.add(u)  # u settle ho gaya: dist[u] final hai
        order.append(u)
        for v in graph[u]:  # har neighbour relax karo (weight = 1)
            if dist[u] + 1 < dist[v]:
                dist[v] = dist[u] + 1
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, prev, order


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
    dist, prev, order = dijkstra(GRAPH_1, SOURCE)
    print("Settle order:", ' -> '.join(order))
    print("\nShortest distances from", SOURCE, "(edge weight = 1):")
    for v in sorted(dist):
        print(f"  {SOURCE} -> {v} = {dist[v]}")
    path = reconstruct_path(prev, SOURCE, TARGET)
    print(f"\nShortest path {SOURCE} -> {TARGET}: {' -> '.join(path)} "
          f"(distance {dist[TARGET]})")
    print("All distances from A: " +
          ", ".join(f"{v}={dist[v]}" for v in sorted(dist)))
