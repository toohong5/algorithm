import sys
sys.stdin = open('minsum.txt', 'r')
from collections import deque
def BFS(x, y, sum1):
    q = deque()
    q.append([x, y, sum1])
    dx = [1, 0] # 하 우
    dy = [0, 1]
    while q:
        n = q.popleft()
        x, y, s = n[0], n[1], n[2]
        for i in range(2):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 < N and 0 <= y1 < N:
                if visit[x1][y1] == 0:
                    visit[x1][y1] = s + arr[x1][y1]
                    q.append([x1, y1, s + arr[x1][y1]])
                elif visit[x1][y1] > s + arr[x1][y1]:
                    visit[x1][y1] = s + arr[x1][y1]
                    q.append([x1, y1, s + arr[x1][y1]])
                elif visit[x1][y1] == s + arr[x1][y1]:
                    q.append([x1, y1, s + arr[x1][y1]])
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    BFS(0, 0, arr[0][0])
    print(visit)
    print('#{} {}'.format(tc, visit[-1][-1]))