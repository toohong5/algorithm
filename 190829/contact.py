import sys
sys.stdin = open('sample_input5.txt', 'r')
from collections import deque

def BFS(start):
    visit = [0] * 101
    q = deque()
    q.append(start)
    visit[start] = 1
    end = []

    while q:
        v = q.popleft()
        for w in G[v]:
            if not visit[w]:
                visit[w] = visit[v] + 1
                q.append(w)
    max_num = 0
    for v in visit:
        if v >= max_num:
            max_num = v
    for v in range(len(visit)):
        if max_num == visit[v]:
            end.append(v)
    print(visit)
    return end


for tc in range(1, 11):
    length, start = map(int, input().split())
    G = [[] for _ in range(101)]
    
    arr = list(map(int, input().split()))
    for _ in range(length//2):
        u = arr.pop(0)
        v = arr.pop(0)
        G[u].append(v)
    print('#{} {}'.format(tc, max(BFS(start))))