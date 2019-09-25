import sys
sys.stdin = open('min_sum.txt', 'r')

def minsum(sum, row):
    global min_sum
    if min_sum < sum:
        return
    if row == N:
        min_sum = min(min_sum, sum)
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            minsum(sum + arr[row][i], row + 1)
            visit[i] = 0
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N

    min_sum = 5000000
    minsum(0, 0)
    print('#{} {}'.format(tc, min_sum))

