import sys
sys.stdin = open('contact.txt', 'r')
from collections import deque

def BFS(s):
    visit = [0] * 101
    q = deque()
    q.append(s)
    visit[s] = 1
    while q:
        v = q.popleft()
        for w in G[v]:
            if not visit[w]:
                visit[w] = visit[v] + 1
                q.append(w)
    max_visit = max(visit)
    max_num = 0
    for i in range(len(visit)):
        if visit[i] == max_visit:
            if max_num <= i:
                max_num = i
    return max_num

for tc in range(1, 11):
    N, S = map(int, input().split())
    G = [[] for _ in range(101)]
    arr = list(map(int, input().split()))
    max_num = 0
    for i in range(N//2):
        u = arr.pop(0)
        v = arr.pop(0)
        G[u].append(v)
    print('#{} {}'.format(tc, BFS(S)))