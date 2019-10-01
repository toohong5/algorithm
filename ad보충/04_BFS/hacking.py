import sys
sys.stdin = open('hacking.txt', 'r')

from collections import deque

def BFS(s):
    global max_count
    q = deque()
    q.append(s)
    visit[s] = 1
    count = 1
    while q:
        v = q.popleft()
        for w in G[v]:
            q.append(w)
            count += 1
    if count >= max_count:
        max_count = count
        idx_list.append(s)
        
V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
visit = [0] * (V + 1)
for _ in range(E):
    u, v = map(int, input().split())
    G[v].append(u)
max_count = 0
idx_list = []
for i in range(1, V + 1):
    if not visit[i]:
        BFS(i)
print(*idx_list)