import sys
sys.stdin = open('village.txt', 'r')

def DFS(v):
    visit[v] = 1
    for w in G[v]:
        if not visit[w]:
            DFS(w)

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    visit = [0] * (V + 1)
    u_list = []
    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
        u_list.append(u)
    result = 0
    for i in range(1, V + 1):
        if not visit[i]:
            DFS(i)
            result += 1
    print('#{} {}'.format(tc, result))