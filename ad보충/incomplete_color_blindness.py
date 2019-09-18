import sys
from pprint import pprint
sys.stdin = open('incomplete_color_blindness.txt', 'r')
# sys.setrecursionlimit(10**8)

def DFS(x, y, c):
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]
    visit1[x][y] = 1
    visit2[x][y] = 1
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < N and 0 <= y1 < N:
            if not visit1[x1][y1] and not visit2[x1][y1]:
                if arr[x1][y1] == c:
                    DFS(x1, y1, c)

N = int(input())
arr = [list(input()) for _ in range(N)]
# pprint(arr)
visit1 = [[0] * N for _ in range(N)]
visit2 = [[0] * N for _ in range(N)]
result1 = 0
result2 = 0
for i in range(N):
    for j in range(N):
        if not visit1[i][j] and not visit2[i][j]:
            if arr[i][j] == 'R':
                DFS(i, j, 'R')
                result1 += 1
                result2 += 1
            if arr[i][j] == 'B':
                DFS(i, j, 'B')
                result1 += 1
                result2 += 1
            if arr[i][j] == 'G':
                DFS(i, j, 'G')
                result1 += 1
print(result1, result2)