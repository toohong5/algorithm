import sys
sys.stdin = open('min_sum.txt', 'r')
from collections import deque

def bfs(x, y, sum):
    q = deque()
    q.append([x, y, sum])
    dx = [1, 0] # 하, 우
    dy = [0, 1]
    while q:
        x, y, sum = q.pop()
        for i in range(2):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 < N and 0 <= y1 < N:
                if visit[x1][y1] == 0:
                    visit[x1][y1] = sum + arr[x1][y1]
                    q.append([x1, y1, sum + arr[x1][y1]])
                elif visit[x1][y1] > sum + arr[x1][y1]:
                    visit[x1][y1] = sum + arr[x1][y1]
                    q.append([x1, y1, sum + arr[x1][y1]])
                elif visit[x1][y1] == sum + arr[x1][y1]:
                    q.append([x1, y1, sum + arr[x1][y1]])
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    bfs(0, 0, arr[0][0])
    print(visit[-1][-1])