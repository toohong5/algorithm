import sys
sys.stdin = open('virus.txt', 'r')

def DFS(v):
    global count
    visit[v] = 1
    for w in G[v]:
        if not visit[w]:
            count += 1
            DFS(w)
V = int(input())
E = int(input())
visit = [0] * (V + 1)
G = [[] for _ in range(V+1)]
count = 0
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
DFS(1)
print(count)
