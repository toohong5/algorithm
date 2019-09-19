import sys
from pprint import pprint
sys.stdin = open('incomplete_color_blindness.txt', 'r')
# sys.setrecursionlimit(10**8)

def DFS(x, y, c):
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]
    visit1[x][y] = 1
    # visit2[x][y] = 1
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < N and 0 <= y1 < N:
            if not visit1[x1][y1]:
                if arr[x1][y1] == c:
                    # print(c)
                    DFS(x1, y1, c)
# def DFS2(x, y, c):
#     dx = [-1, 1, 0, 0] # 상하좌우
#     dy = [0, 0, -1, 1]
#     # visit1[x][y] = 1
#     visit2[x][y] = 1
#     # print(c)
#     for i in range(4):
#         x1 = x + dx[i]
#         y1 = y + dy[i]
#         if 0 <= x1 < N and 0 <= y1 < N:
#             if not visit2[x1][y1]:
#                 if arr[x1][y1] == 'G' and c == 'R':
#                     DFS2(x1, y1, c)
#                 if arr[x1][y1] == c:
#                     # print(c)
#                     DFS2(x1, y1, c)
N = int(input())
arr = [list(input()) for _ in range(N)]
visit1 = [[0] * N for _ in range(N)]
# pprint(arr)
# visit2 = [[0] * N for _ in range(N)]
result1 = 0
result2 = 0
for i in range(N):
    for j in range(N):
        if not visit1[i][j]:
            DFS(i, j, arr[i][j])
            result1 += 1
visit1 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
                arr[i][j] = 'R'
for i in range(N):
    for j in range(N):
        if not visit1[i][j]:
            DFS(i, j, arr[i][j])
            result2 += 1
print(result1, result2)
            

# for i in range(N):
#     for j in range(N):
#         if not visit1[i][j]:
#             if arr[i][j] != 'B':
#                 DFS(i, j, 'R')
#                 result2 += 1
#             else:
#                 DFS(i, j, 'B')
#                 result2 += 1