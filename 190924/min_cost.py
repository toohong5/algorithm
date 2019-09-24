import sys
sys.stdin = open('min_cost.txt', 'r')

def min_sum(sum, row):
    global mini
    if sum > mini:
        return
    if row == N and sum < mini:
        mini = sum
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            min_sum(sum + arr[row][i], row + 1)
            visit[i] = 0
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    mini = 50000000
    min_sum(0, 0)
    print('#{} {}'.format(tc, mini))
