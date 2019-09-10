import sys
sys.stdin = open('break.txt', 'r')
from collections import deque

def DFS(x, y):
    # S = []
    # S.append([x, y])
    result = 0
    visit = [[0] * M for _ in range(N)]
    global distance
    global num_break
    visit[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # if arr[x][y] == 2:
    #     distance += 1
    #     return 1
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < N and 0 <= y1 < M:
            if not visit[x1][y1]:
                if arr[x1][y1] == 0:
                    distance += 1
                    DFS(x1, y1)
                if arr[x1][y1] == 1 and num_break != 0:
                    num_break = 0
                    distance += 1
                    arr[x1][y1] = 0
                    DFS(x1, y1)
                if arr[x1][y1] == 2:
                    distance += 1
                    result = 1
                    return result


# def BFS(arr, x, y, distance):
#     visit = [[0] * M for _ in range(N)]
#     q = deque()
#     q.append([x, y, distance])
#     visit[x][y] = 1
#     global count
#     num_break = 1
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     # if  
#     while q:
#         n = q.popleft()
#         x , y = n[1], n[2]
#         for i in range(4):
#             x1 = x + dx[i]
#             y1 = y + dy[i]
#             if 0 <= x1 < N and 0 <= y1 < M:
#                 if not visit[x1][y1]:
#                     if arr[x1][y1] == 0:
#                         visit[x1][y1] = 1
#                         q.append([x1, y1, n[3] + 1])
#                     if arr[x1][y1] == 1 and num_break != 0:
#                         BFS(arr, x1, y1, n[3] + 1)
#                         arr[x1][y1] = 0
#                         BFS(arr, x1, y1, n[3] + 1)
#                         num_break -= 1
#                         visit[x1][y1] = 1
#                         q.append([x1, y1, n[3] + 1])
#                         # arr[x1][y1] = 0
#                         # for j in range(4):
#                         #     x1 = x1 + dx[j]
#                         #     y1 = y1 + dy[j]
#                         #     if 0 <= x1 < N and 0 <= y1 < M:
#                         #         if not visit[x1][y1]:
#                         #             if arr[x1][y1] == 0:
#                         #                 visit[x1][y1] = 1
#                         #                 q.append([x1, y1, n[2] + 2])
#                         #             if arr[x1][y1] == 2:
#                         #                 count = min(count, n[2] + 1)
#                         #                 return 1
#                         # else:
#                         #     break
#                     if arr[x1][y1] == 2:
#                         count = min(count, n[2] + 1)
#                         return 1
#     return 0

N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
arr[N-1][M-1] = 2
count = 50000
distance = 1
num_break = 1
# print(arr)
DFS(0, 0)
print(distance)


# BFS(arr, 0, 0, 1)
# if BFS(arr, 0, 0, 1):
#     print(count)
#     print(arr)
# else:
#     print(-1)
#     print(arr)