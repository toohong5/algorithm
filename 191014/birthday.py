import sys
sys.stdin = open('birthday.txt', 'r')

from collections import deque
def BFS(s):
    q = deque()
    visit[s] = 1
    q.append(s)
    while q:
        v = q.popleft()
        for w in G[v]:
            if not visit[w]:
                q.append(w)
                visit[w] = visit[v] + 1

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    visit = [0] * (N + 1)
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    BFS(1)
    cnt = 0
    for i in visit:
        if i == 2 or i == 3:
            cnt += 1
    print('#{} {}'.format(tc, cnt))