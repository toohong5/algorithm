import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    row = col = 0
    for i in range(N):
        row += 1
        for j in range(N):
            if arr[i][j] != 0:
                arr[i][j] = 0
                col += 1