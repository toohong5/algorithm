import sys
sys.stdin = open('5248.txt', 'r')

from collections import deque
def BFS(s):
    q = deque()
    q.append(s)
    visit[s] = 1
    while q:
        v = q.popleft()
        for w in G[v]:
            if not visit[w]:
                q.append(w)
                visit[w] = 1

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    G = [[] for _ in range(n + 1)]
    arr = list(map(int, input().split()))
    visit = [0] * (n + 1)
    for i in range(0, len(arr), 2):
        G[arr[i]].append(arr[i + 1])
        G[arr[i + 1]].append(arr[i])
    
    cnt = 0
    for start in range(1, n + 1):
        if not visit[start]:
            BFS(start)
            cnt += 1
    print('#{} {}'.format(tc, cnt))