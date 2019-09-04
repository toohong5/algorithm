import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            sum = 0
            for x in range(r, r + M):
                for y in range(c, c + M):
                    sum += arr[x][y]
            if sum > max_sum:
                max_sum = sum
    print('#{} {}'.format(tc, max_sum))