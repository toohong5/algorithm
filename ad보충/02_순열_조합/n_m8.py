import sys
sys.stdin = open('n_m5.txt', 'r')

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
choose = []
def perm(k, n):
    if k == n:
        print(*choose)
        return
    for i in range(N):
        if len(choose) == 0:
            choose.append(arr[i])
            perm(k + 1, n)
            choose.pop()
        elif choose[-1] <= arr[i]:
            choose.append(arr[i])
            perm(k + 1, n)
            choose.pop()
perm(0, M)
