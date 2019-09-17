import sys
sys.stdin = open('cart.txt', 'r')

def perm(sum1, row):
    global mini
    if sum1 > mini:
        return
    if row == N and sum1 < mini:
        mini = sum1
        return
    else:
        j = 0
        for i in range(N):
            if row == N - 1:
                perm(sum1 + arr[row][0], row + 1)
            if visit[i] == 0 and i != row:
                visit[i] = 1
                j = i
                perm(sum1 + arr[row][i], row + 1)
                visit[i] = 0
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    mini = 5000000
    perm(0, 0)
    print('#{} {}'.format(tc, mini))