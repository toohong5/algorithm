import sys
sys.stdin = open('russia.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    S = []
    for i in range(1, N - 1):
        for j in range(1, N - i):
            S.append([i, j, N-i-j])
    count_list = []
    for num in S:
        w = num[0]
        b = num[1]
        r = num[2]
        count = 0
        for i in range(N):
            for j in range(M):
                if w > 0 and arr[i][j] != 'W':
                    count += 1
            w -= 1
            if w == 0:
                for p in range(i + 1, N):
                    for q in range(M):
                        if b > 0 and arr[p][q] != 'B':
                            count += 1
                    b -= 1
                    if b == 0:
                        for n in range(p + 1, N):
                            for m in range(M):
                                if arr[n][m] != 'R':
                                    count += 1
                        count_list.append(count)
        
    print('#{} {}'.format(tc, min(count_list)))