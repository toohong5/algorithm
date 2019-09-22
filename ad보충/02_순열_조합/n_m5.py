import sys
sys.stdin = open('n_m5.txt', 'r')

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visit = [0] * N
choose = []
def perm(k, n):
    if k == M:
        # choose.sort()
        print(*choose)
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            choose.append(arr[i])
            perm(k + 1, n)
            choose.pop()
            visit[i] = 0

perm(0, M)