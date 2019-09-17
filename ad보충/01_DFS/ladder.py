import sys
sys.stdin = open('ladder.txt', 'r')
sys.setrecursionlimit(10**6)

def DFS(x, y):
    dx = [0, 0, -1]  # 좌우상
    dy = [-1, 1, 0]
    visit[x][y] = 1
    global fy
    if x == 0:
        fy = y
        return 1
    for i in range(3):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < 100 and 0 <= y1 < 100:
            if not visit[x1][y1]:
                if arr[x1][y1] == 1:
                    DFS(x1, y1)
                    break
                
for tc in range(10):
    visit = [[0] * 100 for _ in range(100)]
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    x = y = 0
    fx = fy = 0
    for i in range(100):
        if 2 in arr[i]:
            x = i
            y = arr[i].index(2)
    DFS(x, y)
    print('#{} {}'.format(N, fy))