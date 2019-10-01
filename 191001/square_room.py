import sys
sys.stdin = open('square_room.txt', 'r')
from collections import deque

def BFS(x, y, array):
    global idx, max_count
    q = deque()
    q.append([x, y, array])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y, array = q.popleft()
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if  0 <= x1 < N and 0 <= y1 < N:
                if arr[x1][y1] == arr[x][y] + 1:
                    array.append(arr[x1][y1])
                    q.append([x1, y1, array])
    if len(array) > max_count:
        max_count = len(array)
        idx = array[0]
    if len(array) == max_count:
        if array[0] < idx:
            idx = array[0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 1
    max_count = 0
    idx = 50000000000
    for i in range(N):
        for j in range(N):
                BFS(i, j, [arr[i][j]])

    print('#{} {} {}'.format(tc, idx, max_count))