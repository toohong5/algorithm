import sys
sys.stdin = open('input_rotate.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    arr_new = []

    for _ in range(3):
        for i in range(N):
            for j in range(i, N):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        for row in arr:
            row.reverse()

        for i in range(N):
            w = ''
            for j in range(N):
                w += arr[i][j]
            arr_new.append(w)

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(i, i + (3*N), N):
            print(arr_new[j], end=' ')
        print()