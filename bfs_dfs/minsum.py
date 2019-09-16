import sys
sys.stdin = open('minsum.txt', 'r')
from collections import deque
def DFS(x, y, sum1):
    dx = [1, 0] # 하 우
    dy = [0, 1]
    x1 = x + dx[0]
    y1 = y + dy[0]
    x2 = x + dx[1]
    y2 = y + dy[1]
    if x == N - 1 and y == N - 1:
        sum1 += arr[x][y]
        S.append(sum1)
        return 1
    if x1 == N - 1 and y1 == N - 1:
        sum1 += arr[x1][y1]
        # min_sum = min(min_sum, sum1)
        S.append(sum1)
        return 1
    if x2 == N - 1 and y2 == N - 1:
        sum1 += arr[x2][y2]
        # min_sum = min(min_sum, sum1)
        S.append(sum1)
        return 1
    else:
        if (0<=x1<N and 0<=y1<N) and (x2<0 or x2>=N or y2<0 or y2>=N):
            sum1 += arr[x1][y1]
            DFS(x1, y1, sum1)
        if (0<=x2<N and 0<=y2<N) and (x1<0 or x1>=N or y1<0 or y1>=N):
            sum1 += arr[x2][y2]
            DFS(x2, y2, sum1)
        if 0<=x1<N and 0<=y1<N and 0<=x2<N and 0<=y2<N:
            # if x1 == N - 1 and y1 == N - 1:
            #     sum1 += arr[]
            if arr[x1][y1] > arr[x2][y2]:
                # sum1 += arr[x2][y2]
                DFS(x2, y2, sum1 + arr[x2][y2])
            elif arr[x1][y1] == arr[x2][y2]:
                DFS(x1, y1, sum1 + arr[x1][y1])
                DFS(x2, y2, sum1 + arr[x2][y2])
            else:
                sum1 += arr[x1][y1]
                DFS(x1, y1, sum1)
        # for i in range(2):
        #     x1 = x + dx[i]
        #     y1 = y + dy[i]
        #     if 0 <= x1 < N and 0 <= y1 < N:
        #         if arr[x1][y1] >= arr[x + dx[]]
        #         if x1 == N - 1 and y1 == N - 1:
        #             sum1 += arr[x1][y1]
        #             min_sum = min(min_sum, sum1)
        #         else:
        #             sum1 += 
def BFS(x, y, sum1):
    global min_sum
    q = deque()
    q.append([x, y, sum1])
    dx = [1, 0] # 하 우
    dy = [0, 1]
    while q:
        n = q.popleft()
        x = n[0]
        y = n[1]
        for i in range(2):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 < N and 0 <= y1 < N:
                if x1 == N - 1 and y1 == N - 1:
                    min_sum = min(min_sum, n[2] + arr[x1][y1])
                else:
                    if n[2] + arr[x1][y1] < min_sum:
                        q.append([x1, y1, n[2] + arr[x1][y1]])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    S = [500000]
    min_sum = 5000000000
    DFS(0, 0, arr[0][0])
    print('#{} {}'.format(tc, min(S)))
    