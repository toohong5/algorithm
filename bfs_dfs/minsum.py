import sys
sys.stdin = open('minsum.txt', 'r')
from collections import deque

def BFS(x, y, sum1):
    global min_sum
    q = deque()
    q.append([x, y, sum1])
    dx = [1, 0] # 하 우
    dy = [0, 1]
    while q:
        n = q.popleft()
        x = n[0]
        y = n[1]
        for i in range(2):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 < N and 0 <= y1 < N:
                if x1 == N - 1 and y1 == N - 1:
                    min_sum = min(min_sum, n[2] + arr[x1][y1])
                else:
                    if n[2] + arr[x1][y1] < min_sum:
                        q.append([x1, y1, n[2] + arr[x1][y1]])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 5000000000
    BFS(0, 0, arr[0][0])
    print('#{} {}'.format(tc, min_sum))
    