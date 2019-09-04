import sys
sys.stdin = open('sample_input4.txt', 'r')

def DFS(v):
    visit = [0] * (V + 1)
    global S
    S.append(v)
    visit[v] = 1
    for w in G[v]:
        if len(g2[w]) > 1 and v in g2[w]:
            g2[w].remove(v)
            continue
        if not visit[w]:
            DFS(w)

for tc in range(1, 11):
    S = []
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    g2 = [[] for _ in range(V + 1)]
    w_list = []
    arr = list(map(int, input().split()))
    for _ in range(len(arr)//2):
        u = arr.pop(0)
        v = arr.pop(0)
        G[u].append(v)
        g2[v].append(u)

    for k in range(1, len(g2)):
        if len(g2[k]) == 0:
            DFS(k)
    print('#{}'.format(tc), *S)