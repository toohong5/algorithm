import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, K= map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            # count2 = 0
            if arr[i][j] == 1:
                count1 = 0
                # for n in range(N):
                for k in range(j, N):
                    if arr[i][k] == 1:
                        count1 += 1
                    else:
                        if count1 == K:
                            result += 1
                        count1 = 0
                    if k == N - 1:
                        if count1 == K:
                            result += 1
                        count1 = 0
                break

    for j in range(N):
        for i in range(N):
            if arr[i][j] == 1:
                count2 = 0
                # for n in range(N):
                for k in range(i, N):
                    if arr[k][j] == 1:
                        count2 += 1
                    else:
                        if count2 == K:
                            result += 1
                        count2 = 0
                    if k == N - 1:
                        if count2 == K:
                            result += 1
                        count2 = 0
                break
    print('#{} {}'.format(tc, result))