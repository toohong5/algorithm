import sys
from collections import deque
sys.stdin = open('dfs_bfs.txt', 'r')

def DFS(v):
    visit_d[v] = 1
    print(v, end=' ')
    for w in G[v]:
        if not visit_d[w]:
            s.append(w)
            DFS(w)

def BFS(v):
    visit_b[v] = 1
    q.append(v)
    
    while q:
        v = q.popleft()
        for w in G[v]:
            if not visit_b[w]:
                q.append(w)
                visit_b[w] = 1
        print(v, end=' ')

V, E, S = map(int, input().split())

visit_d = [0] * (V + 1)
visit_b = [0] * (V + 1)

G = [[] for _ in range(V+1)]
s = []
q = deque()
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
for _ in range(len(G)):
    row = sorted(G.pop(0))
    G.append(row)

DFS(S)
print()
BFS(S)