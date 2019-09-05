import sys
sys.stdin = open('input4.txt', 'r')

def DFS(x, y, dx, dy):
    visit[x][y] = 1
    x1 = x + dx
    y1 = y + dy
    if 0 <= x1 < N and 0 <= y1 < N:
        if not visit[x1][y1]:
            if arr[x][y] != 0:
                if arr[x][y] == arr[x1][y1]:
                    arr[x][y] += arr[x1][y1]
                    arr[x1].pop(y1)
                    arr[x1].append(0)
                    DFS(x1, y1, dx, dy)
                else:
                    DFS(x1, y1, dx, dy)
            if arr[x][y] == 0:
                if arr[x1][y1] == 0:
                    DFS(x1, y1, dx, dy)
                else:
                    arr[x][y] += arr[x1][y1]
                    arr[x1][y1] = 0
                    DFS(x1, y1, dx, dy)

T = int(input())
for tc in range(1, T + 1):
    N, way = input().split()
    N = int(N)
    S = []
    visit = [[0] * N for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    delta_x = [1, -1, 0, 0] # up, down, right, left
    delta_y = [0, 0, -1, 1] # up, down, right, left

    if way == 'up':
        dx = delta_x[3]
        dy = delta_y[3]

        for i in range(N):
            for j in range(i, N):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        for row in arr:
            for j in range(len(row)):
                if row[j] == 0:
                    row.pop(j)
                    row.append(0)
                    for k in range(j, len(row)):
                        if row[j] == 0:
                            row.pop(j)
                            row.append(0) 

        for i in range(N):
            x = i
            y = 0
            DFS(x, y, dx, dy)

        for i in range(N):
            for j in range(i, N):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    if way == 'down':
        dx = delta_x[3]
        dy = delta_y[3]

        for i in range(N):
            for j in range(i, N):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        for row in arr:
            row.reverse()
        for row in arr:
            for j in range(len(row)):
                if row[j] == 0:
                    row.pop(j)
                    row.append(0)
                    for k in range(j, len(row)):
                        if row[j] == 0:
                            row.pop(j)
                            row.append(0)  
        for i in range(N):
            x = i
            y = 0
            DFS(x, y, dx, dy)
        for row in arr:
            row.reverse()    
        for i in range(N):
            for j in range(i, N):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    if way == 'right':
        dx = delta_x[3]
        dy = delta_y[3]
        for row in arr:
            row.reverse()
        for row in arr:
            for j in range(len(row)):
                if row[j] == 0:
                    row.pop(j)
                    row.append(0)
                    for k in range(j, len(row)):
                        if row[j] == 0:
                            row.pop(j)
                            row.append(0)
        for i in range(N):
            x = i
            y = 0
            DFS(x, y, dx, dy)
        for row in arr:
            row.reverse()

    if way == 'left':
        dx = delta_x[3]
        dy = delta_y[3]
        for row in arr:
            for j in range(len(row)):
                if row[j] == 0:
                    row.pop(j)
                    row.append(0)
                    for k in range(j, len(row)):
                        if row[j] == 0:
                            row.pop(j)
                            row.append(0)
        for i in range(N):
            x = i
            y = 0
            DFS(x, y, dx, dy)

    print('#{}'.format(tc))
    for row in arr:
        print(*row)