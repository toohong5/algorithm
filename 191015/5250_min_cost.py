import sys
sys.stdin = open('5250.txt', 'r')

from collections import deque
def BFS(x, y):
    q = deque()
    q.append((x, y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 < n and 0 <= y1 < n:
                diff = 0 if arr[x1][y1] <= arr[x][y] else arr[x1][y1] - arr[x][y]
                if arr_sum[x1][y1] == 0:
                    arr_sum[x1][y1] = arr_sum[x][y] + diff + 1
                    q.append((x1, y1))
                elif arr_sum[x][y] + diff + 1 < arr_sum[x1][y1]:
                    arr_sum[x1][y1] = arr_sum[x][y] + diff + 1
                    q.append((x1, y1))

for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_sum = [[0] * n for _ in range(n)]
    BFS(0, 0)
    print('#{} {}'.format(tc, arr_sum[-1][-1]))