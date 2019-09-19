import sys
sys.stdin = open('russia.txt', 'r')

def DFS(x, y, c):
    global count_w
    global count_b
    global count_r
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visit[x][y] = 1
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < N and 0 <= y1 < M:
            if not visit[x1][y1]:
                if arr[x1][y1]=='W':
                    count_w += 1
                    DFS(x1, y1, 'W')
                if arr[x1][y1]=='B':
                    count_b += 1
                    DFS(x1, y1, 'B')
                if arr[x1][y1]=='R':
                    count_r += 1
                    DFS(x1, y1, 'R')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    count_w = 1
    count_b = 0
    count_r = 0
    visit = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visit[i][j]:
                DFS(i, j, arr[i][j])

    print(count_w, count_b, count_r)