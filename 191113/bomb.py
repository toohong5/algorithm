import sys
sys.stdin = open('bomb.txt', 'r')
from pprint import pprint
def stars(x, y):
    cnt = 0
    for i in range(8):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < N and 0 <= y1 < N:
            if not visit[x1][y1]:
                if arr[x1][y1] == -1 or arr[x1][y1] == '*':
                    cnt += 1
    return cnt

def DFS(x, y):
    for k in range(8):
        x1 = x + dx[k]
        y1 = y + dy[k]
        if 0 <= x1 < N and 0 <= y1 < N:
            if not visit[x1][y1]:
                if arr[x1][y1] == 0:
                    visit[x1][y1] = 1
                    DFS(x1, y1)
                elif arr[x1][y1] != -1 and arr[x1][y1] != 0:
                    visit[x1][y1] = 1
                    
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    dx = [-1, 1, 0, 0, -1, 1, -1, 1] # 상 하 좌 우 우상 우하 좌상 좌하
    dy = [0, 0, -1, 1, 1, 1, -1, -1] # 상 하 좌 우 우상 우하 좌상 좌하
    visit = [[0] * N for _ in range(N)]
    # 8방향 별의 개수 -> dfs(한꺼번에 펼쳐지는 영역 탐색)
    for x in range(N):
        for y in range(N):
            if arr[x][y] == '*':
                arr[x][y] = -1
            else:
                arr[x][y] = stars(x, y)
    count = 0
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                if arr[i][j] == 0:
                    visit[i][j] = 1
                    DFS(i, j)
                    count += 1
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0 and arr[i][j] != -1:
                count += 1
    print('#{} {}'.format(tc, count))