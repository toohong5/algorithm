import sys
sys.stdin = open('max_prize.txt', 'r')

def perm(k, n, count):
    global max_prize
    if k == n:
        change = 0
        for i in range(n):
            if choose[i] != arr[i]:
                change += 1
        if change - 1 == count:
            w = ''.join(choose)
            max_prize = max(max_prize, int(w))
        return
    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            choose.append(arr[i])
            perm(k + 1, n, count)
            choose.pop()
            visit[i] = 0

T = int(input())
for tc in range(1, T + 1):
    arr, N = map(int, input().split())
    arr = list(str(arr))
    visit = [0] * len(arr)
    choose = []
    max_prize = 0
    perm(0, len(arr), N)
    print('#{} {}'.format(tc, max_prize))