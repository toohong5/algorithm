import sys
sys.stdin = open('island.txt', 'r')
from collections import deque

def BFS(x, y):
    visit = [[0] * N for _ in range(N)]
    q = deque()
    visit[x][y] = 1
    q.append([x, y])
    while q:
        n = q.popleft()
        for i in range(8):
            x1 = n[0] + dx[i]
            y1 = n[1] + dy[i]
            if 0 <= x1 < N and 0 <= y1 < N:
                if not visit[x1][y1]:
                    if arr[x1][y1] != 0:
                        visit[x1][y1] = 1
                        arr[x1][y1] = 0
                        q.append([x1, y1])
    return 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 1, 0, 0, -1, 1, -1, 1] # 상 하 좌 우 좌상 좌하 우상 우하
    dy = [0, 0, -1, 1, -1, -1, 1, 1]
    count = 0
    x = y = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                x = i
                y = j
                count += BFS(x, y)

    print('#{} {}'.format(tc, count))