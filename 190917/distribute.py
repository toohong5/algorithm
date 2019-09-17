import sys
sys.stdin = open('input.txt', 'r')

def perm(per, row):
    global maximum
    if per * 100 <= maximum:
        return
    if row == N and (per * 100 > maximum):
        maximum = per * 100
        return 
    else:
        for i in range(N):
            if visit[i] == 0:
                visit[i] = 1
                perm(per * arr[row][i], row + 1)
                visit[i] = 0

T = int(input())
for tc in range(1, T + 1):
    visit = [0] * 17
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maximum = 0
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] / 100

    perm(1.0, 0)
    print('#%d %.6f'%(tc, maximum))