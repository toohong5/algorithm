import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    arr[0][0] = 1

    for i in range(1, N):
        for j in range(1, N):
            arr[j][0] = 1
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
    print('#{}'.format(tc))
    for row in arr:
        for n in row:
            if n != 0:
                print(n, end=' ')
        print()

    
