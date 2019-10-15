import sys
sys.stdin = open('5249.txt', 'r')
from collections import deque
def BFS(s):
    global weight
    q = deque()
    D = [0xffffff for _ in range(V + 1)]
    P = [0 for _ in range(V + 1)]
    D[s] = 0
    P[s] = s

    q.append(s)
    while q:
        u = q.popleft()
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                weight += w
                P[v] = u
                q.append(v)
    print(D)
    print(P)
    # for i in range(len(P) - 1, 0, -1):
    #     P[i]

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        G[n1].append((n2, w))
        G[n2].append((n1, w))
    print(G)
    weight = 0
    BFS(0)
    print(weight)
    print()