# Exp 10 - Map Colouring problem (backtracking)
# Graph 1 (FAT exam) ke vertices ko aise colour karo ki koi bhi 2
# connected (adjacent) vertices ka colour same na ho.
# Backtracking: ek-ek vertex ko colour try karo, agar clash ho to
# wapas jao (backtrack) aur agla colour try karo.

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

COLOURS = ["Red", "Green", "Blue"]  # 3 colours (Graph 1 me triangles hain, isliye 2 kaafi nahi)
nodes = list(GRAPH_1.keys())
answer = {}  # har vertex ka colour


# kya vertex v ko colour c de sakte hain?
def safe(v, c):
    for nb in GRAPH_1[v]:  # har padosi ko check karo
        if answer.get(nb) == c:  # padosi ka SAME colour? mana hai!
            return False
    return True


# backtracking se colour karo
def solve(i):
    if i == len(nodes):  # saare vertices coloured - HO GAYA!
        return True
    v = nodes[i]
    for c in COLOURS:  # har colour try karo
        if safe(v, c):
            answer[v] = c  # colour lagao
            if solve(i + 1):  # agle vertex pe jao
                return True
            del answer[v]  # BACKTRACK - colour hatao, wapas jao
    return False


if __name__ == '__main__':
    if solve(0):
        print("Colouring mil gayi!")
        for v in nodes:
            print(f"  Vertex {v} -> {answer[v]}")
        # verify: koi 2 adjacent vertices ka colour same to nahi?
        ok = all(answer[u] != answer[v]
                 for u in GRAPH_1 for v in GRAPH_1[u])
        print("\nVerification: no adjacent vertices share a colour -", ok)
    else:
        print(f"{len(COLOURS)} colours se nahi ho paya - aur colours try karo!")
