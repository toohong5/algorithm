import sys
sys.stdin = open('maze.txt', 'r')
from collections import deque

def BFS(x, y, distance):
    q = deque()
    visit[x][y] = 1
    q.append([x, y, distance])
    global count
    while q:
        n = q.popleft()
        x = n[0]
        y = n[1]
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 < N and 0 <= y1 < M:
                if not visit[x1][y1]:
                    if maze[x1][y1] == 2:
                        count = min(n[2] + 1, count)
                        
                    elif maze[x1][y1] == 1:
                        q.append([x1, y1, n[2]+1])
                        visit[x1][y1] = 1

N, M = map(int, input().split())
visit = [[0] * M for _ in range(N)]
maze = [list(map(int, input())) for _ in range(N)]
maze[N-1][M-1] = 2
dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1] # 상 하 좌 우
count = 5000
# print(maze)
BFS(0, 0, 1)
print(count)