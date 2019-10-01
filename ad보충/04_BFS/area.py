import sys
sys.stdin = open('area.txt', 'r')
from pprint import pprint
from collections import deque

def DFS(x, y):
    global count
    visit[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < N and 0 <= y1 < M:
            if not visit[x1][y1]:
                if arr[x1][y1] == 0:
                    count += 1
                    DFS(x1, y1)

def BFS(x, y):
    global count
    q = deque()
    q.append([x, y])
    visit[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 < N and 0 <= y1 < M:
                if not visit[x1][y1]:
                    if arr[x1][y1] == 0:
                        visit[x1][y1] = 1
                        q.append([x1, y1])
                        count += 1

N, M, K = map(int, input().split())

arr = [[0] * M for _ in range(N)]
visit = [[0] * M for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[j][i] = 1
count_list = []
result = 0
count = 1
for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            if arr[i][j] == 0:
                BFS(i, j)
                result += 1
                count_list.append(count)
                count = 1
count_list.sort()
print(result)
print(*count_list)