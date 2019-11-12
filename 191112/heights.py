import sys
sys.stdin = open('heights.txt', 'r')
from collections import deque

def BFS(s, array):
    q = deque()
    count = 0
    q.append(s)
    visit[s] = 1
    while q:
        v = q.popleft()
        for w in array[v]:
            if not visit[w]:
                q.append(w)
                visit[w] = 1
                count += 1
    return count

for T in range(int(input())):
    N = int(input())
    M = int(input())
    short = [[] for _ in range(N + 1)]
    tall = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        tall[a].append(b)
        short[b].append(a)
    
    cnt = 0
    # 큰사람 + 작은사람 + 자신 == 전체인원 수
    for i in range(1, N + 1):
        visit = [0] * (N + 1)
        n = BFS(i, tall) + BFS(i, short) + 1
        if n == N:
            cnt += 1
    print('#{} {}'.format(T + 1, cnt))