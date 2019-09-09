import sys
sys.stdin = open('connected_component.txt', 'r')

def DFS(v):
    visit[v] = 1
    S.append(v)
    for w in G[v]:
        if not visit[w]:
            DFS(w)
N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
visit = [0] * (N+1)

S = []
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
count = 0
# visit == 0 일때만 돌기 때문에 dfs 한바퀴 돌고 나면 v에 연결된 모든 애들의 visit==1이 되므로 끝남...
for i in range(1, len(G)):
    if visit[i] == 0:
        count += 1
        DFS(i)
print(count)