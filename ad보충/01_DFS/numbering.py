import sys
sys.stdin = open('numbering.txt', 'r')
from collections import deque
from pprint import pprint
# def BFS(x, y):
#     visit = [[0] * N for _ in range(N)]
#     global count
#     count = 1
#     q = deque()
#     q.append([x, y])
#     visit[x][y] = 1
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
    
#     while q:
#         n = q.popleft()
#         x = n[0]
#         y = n[1]
#         for i in range(4):
#             x1 = x + dx[i]
#             y1 = y + dy[i]
#             if 0 <= x1 < N and 0 <= y1 <N:
#                 if not visit[x1][y1]:
#                     if arr[x1][y1] == 1:
#                         q.append([x1, y1])
#                         visit[x1][y1] = 1
#                         count += 1
#                         arr[x1][y1] = 0

def DFS(x, y):
    global count
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visit[x][y] = 1
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < N and 0 <= y1 < N:
            if not visit[x1][y1]:
                if arr[x1][y1] == 1:
                    count += 1
                    DFS(x1, y1)

N = int(input())
visit = [[0] * N for _ in range(N)]
arr = [list(map(int, input())) for _ in range(N)]
result = 0
x = y = 0
count = 1
count_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            if not visit[i][j]:
                x = i
                y = j
                DFS(x, y)
                result += 1
                count_list.append(count)
                count = 1

# pprint(visit)
print(result)
count_list.sort()
for i in count_list:
    print(i)