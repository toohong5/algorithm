import sys
sys.stdin = open('5251.txt', 'r')

from collections import deque
for tc in range(1, int(input()) + 1):
    n, e = map(int, input().split())
    G = [[] for _ in range(n + 1)]

    for _ in range(e):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
        G[v].append((u, w))
    print(G)
    def BFS(s):
        q = deque()
        q.append(s)
        D = [0xffffff] * (n+1)
        P = [0 for _ in range(n + 1)]
        D[s] = 0
        P[s] = s
        while q:
            u = q.popleft()
            for v, w in G[u]:
                if D[v] > D[u] + w:
                    D[v] = D[u] + w
                    P[v] = u
                    q.append(v)
        print('#{} {}'.format(tc, D[n]))
        print(D)
        print(P)
    BFS(0)