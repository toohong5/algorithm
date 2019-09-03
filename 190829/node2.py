import sys
from collections import deque
sys.stdin = open('sample_input4.txt', 'r')


def BFS(start):
    visit = [0] * (V + 1)
    q = deque()
    q.append(start)
    visit[start] = 1
    global g

    while q:
        v = q.popleft()
        for w in G[v]:
            if not visit[w]:
                q.append(w)
                visit[w] = visit[v] + 1
            if w == g:
                return visit[w] - 1
    return visit[g]                 # while문 끝난 뒤 s, g서로 연결 안되어있으면 출력

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    
    s, g = map(int, input().split())

    print('#{} {}'.format(tc, BFS(s)))
