import sys
sys.stdin = open('connected_component.txt', 'r')

def DFS(v):
    # if not visit[v]:
    visit[v] = 1
    S.append(v)
    # print(v)
    for w in G[v]:
        if not visit[w]:
            # S.append(w)
            DFS(w)
    # else:
    #     return 1
N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
visit = [0] * (N+1)

S = []
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
k = []
for i in range(1, len(G)):
    DFS(i)
    if len(S) > 1:
        k.append(S)
    S = []
print(len(k))
# print(count)
