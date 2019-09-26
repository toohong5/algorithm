import sys
from pprint import pprint
sys.stdin = open('knight.txt', 'r')

from collections import deque
def BFS(x, y, cnt):
    global count
    q = deque()
    q.append([x, y, cnt])
    dx = [-2, -1, 2, 1, 1, -2, -1, 2]
    dy = [-1, -2, 1, 2, -2, 1, 2, -1]
    if arr[x][y] == 'a':
        count = min(count, cnt)
        return
    while q:
        x, y, cnt = q.pop()
        if cnt >= count:
            continue
        for i in range(8):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 < N and 0 <= y1 < N:
                if arr[x1][y1] == 'a':
                    count = min(count, cnt+1)
                else:
                    if arr[x1][y1] == 0:
                        arr[x1][y1] = cnt+1
                        q.append([x1, y1, cnt + 1])
                    elif arr[x1][y1] < cnt+1:
                        continue
                    elif arr[x1][y1] > cnt+1:
                        arr[x1][y1] = cnt+1
                        q.append([x1, y1, cnt + 1])
            
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x, y = map(int, input().split()) # 현재 칸
    fx, fy = map(int, input().split()) # 도착 칸
    arr = [[0] * N for _ in range(N)]
    arr[fx][fy] = 'a'
    count = 500000000000
    BFS(x, y, 0)
    print(count)