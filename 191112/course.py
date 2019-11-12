import sys
sys.stdin = open('course.txt', 'r')

def DFS(x, y, cnt, k):
    global long
    if long < cnt:
        long = cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visit[x][y] = 1
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < N and 0 <= y1 < N:
            if not visit[x1][y1]:
                if arr[x1][y1] < arr[x][y]:
                    DFS(x1, y1, cnt + 1, k)
                else:
                    if k:
                        for j in range(1, K + 1):
                            if arr[x1][y1] - j < arr[x][y]:
                                arr[x1][y1] = arr[x1][y1] - j
                                DFS(x1, y1, cnt + 1, False)
                                arr[x1][y1] = arr[x1][y1] + j
    visit[x][y] = 0
                  
# 최대값 찾기
for t in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    max_height = 0
    for row in arr:
        if max_height < max(row):
            max_height = max(row)
    long = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_height:
                DFS(i, j, 0, True)
    print('#{} {}'.format(t, long + 1))