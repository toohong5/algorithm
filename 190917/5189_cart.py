import sys
sys.stdin = open('cart.txt', 'r')
# 순열구하기...
# 
def perm(sum1, row, count):
    global mini
    if sum1 > mini: # MINI보다 크면 끊는다!
        return
    if count == N:
        mini = min(mini, sum1)
        return
    else:
        for i in range(N):
            if i == 0:
                if count == N - 1:
                    perm(sum1 + arr[row][i], i, count + 1)
            else:
                if visit[i] == 0 and i != row:
                    visit[i] = 1
                    perm(sum1 + arr[row][i], i, count + 1)
                    visit[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    mini = 5000000
    perm(0, 0, 0)
    print('#{} {}'.format(tc, mini))