import sys
from pprint import pprint
sys.stdin = open('cabbage.txt', 'r')
sys.setrecursionlimit(10**6)
def DFS(x, y):
    visit[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < n and 0 <= y1 < m:
            if not visit[x1][y1]:
                if arr[x1][y1] == 1:
                    DFS(x1, y1)

T = int(input())
for tc in range(1, T + 1):
    m, n, K = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if not visit[i][j]:
                if arr[i][j] == 1:
                    DFS(i, j)
                    result += 1
    print(result)