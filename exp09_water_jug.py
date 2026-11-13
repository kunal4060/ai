# Exp 9 - Water Jug problem (production system)
# 4 litre aur 3 litre ke jugs se exactly 1 litre measure karo.
# Production rules (6 rules):
#   1. Fill 4-litre jug        2. Fill 3-litre jug
#   3. Empty 4-litre jug       4. Empty 3-litre jug
#   5. Pour 4 -> 3            6. Pour 3 -> 4
# BFS se sabse chhota solution nikalte hain.
# State = (4L jug me paani, 3L jug me paani). Goal: kisi ek me 1 litre.

from collections import deque


def neighbours(state):
    a, b = state  # a = 4L jug, b = 3L jug
    result = []
    # 1. Fill 4-litre jug
    result.append(((4, b), "Fill 4L jug"))
    # 2. Fill 3-litre jug
    result.append(((a, 3), "Fill 3L jug"))
    # 3. Empty 4-litre jug
    result.append(((0, b), "Empty 4L jug"))
    # 4. Empty 3-litre jug
    result.append(((a, 0), "Empty 3L jug"))
    # 5. Pour 4 -> 3 (jitna 3L me jagah hai utna dalo)
    pour = min(a, 3 - b)
    result.append(((a - pour, b + pour), "Pour 4L -> 3L"))
    # 6. Pour 3 -> 4 (jitna 4L me jagah hai utna dalo)
    pour = min(b, 4 - a)
    result.append(((a + pour, b - pour), "Pour 3L -> 4L"))
    return result


def bfs(start, goal_test):
    queue = deque([start])
    visited = {start}
    parent = {start: (None, '')}
    while queue:
        cur = queue.popleft()
        if goal_test(cur):  # goal mil gaya?
            break
        for nxt, rule in neighbours(cur):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = (cur, rule)
                queue.append(nxt)
    # goal se wapas start tak path jodo
    goal = cur
    path, rules = [], []
    node = goal
    while node is not None:
        path.append(node)
        node, rule = parent[node]
        rules.append(rule)
    path.reverse()
    rules.reverse()
    return path, rules[1:]


if __name__ == '__main__':
    start = (0, 0)
    goal_test = lambda s: s[0] == 1 or s[1] == 1  # kisi ek jug me 1 litre
    path, rules = bfs(start, goal_test)
    print("Steps:", len(rules))
    print("\n(4L jug, 3L jug)   | Rule")
    print("-" * 40)
    print(f"  {path[0]}          | Start")
    for i, rule in enumerate(rules):
        print(f"  {path[i + 1]}          | {rule}")
    print(f"\nGoal reached: {path[-1]} - 1 litre measured!")
