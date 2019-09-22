import sys
sys.stdin = open('container.txt', 'r')
sys.setrecursionlimit(10**6)
def perm(k, n):
    global ans
    if k == n:
        num_true = 0
        for i in range(n):
            if capacity[i] >= choose[i]:
                num_true += 1
        if num_true == n:
            ans.append(sum(choose))
        return
    for i in range(len(weight)):
        if not visit[i]:
            visit[i] = 1
            choose.append(weight[i])
            perm(k + 1, n)
            choose.pop()
            visit[i] = 0
def perm2(k, n):
    if k == n:
        sum1 = 0
        for i in range(n):
            if choose[i] >= weight[i]:
                sum1 += weight[i]
        ans.append(sum1)
        return
    for i in range(len(capacity)):
        if not visit[i]:
            visit[i] = 1
            choose.append(capacity[i])
            perm2(k + 1, n)
            choose.pop()
            visit[i] = 0
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # 화물 수, 트럭 수
    choose = []
    ans = []
    weight = list(map(int, input().split()))
    capacity = list(map(int, input().split()))
    visit = [0] * 100
    if N > M:
        perm(0, M)
    else:
        perm2(0, N)
    # if len(ans)
    print('#{} {}'.format(tc, max(ans)))