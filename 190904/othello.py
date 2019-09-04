import sys
sys.stdin = open('input2.txt', 'r')

# 1: 흑 / 2: 백
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    
    arr[N//2 - 1][N//2 - 1] = 2
    arr[N//2][N//2 - 1] = 1
    arr[N//2 - 1][N//2] = 1
    arr[N//2][N//2] = 2
           
    dx = [-1, 1, 0, 0, -1, 1, -1, 1] # 상 하 좌 우 / 우상 우하 좌상 좌하
    dy = [0, 0, -1, 1, 1, 1, -1, -1] # 상 하 좌 우 / 우상 우하 좌상 좌하

    for _ in range(M):
        r, c, color = map(int, input().split())
        r = r - 1
        c = c - 1
        arr[r][c] = color
        for i in range(8):
            count = 0
            x = r + dx[i]
            y = c + dy[i]
            if 0 <= x < N and 0 <= y < N:
                if arr[x][y] != 0 and arr[x][y] != color:       # 색이 다르면...
                    count += 1
                    x1 = x
                    y1 = y
                    while True:
                        x1 = x1 + dx[i]
                        y1 = y1 + dy[i]
                        if 0 <= x1 < N and 0 <= y1 < N:
                            if arr[x1][y1] == color:
                                while count != 0:
                                    x1 = x1 - dx[i]
                                    y1 = y1 - dy[i]
                                    arr[x1][y1] = color
                                    count -= 1
                                break
                            elif arr[x1][y1] != color and arr[x1][y1] != 0:
                                count += 1
                            elif arr[x1][y1] == 0:
                                break
                        else:
                            break
    black = white = 0
    for row in arr:
        # print(row)
        black += row.count(1)
        white += row.count(2) 
    # print()
    print('#{} {} {}'.format(tc, black, white))