import sys
sys.stdin = open('dongcheol.txt', 'r')

def perm(per, row):
    global max_percent
    if per * 100 < max_percent:
        return
    if row == N - 1 and per * 100 > max_percent:
        max_percent = per * 100
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            perm(per * arr[i][j], row + 1)
            visit[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * 17
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] / 100
    max_percent = 0
    perm(1.0, 0)
    print(max_percent)
