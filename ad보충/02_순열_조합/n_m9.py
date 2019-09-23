import sys
sys.stdin = open('n_m9.txt', 'r')

def perm(k, n):
    if k == n:
        a = choose[::]
        if a not in choose_list:
            choose_list.append(a)
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            choose.append(arr[i])
            perm(k + 1, n)
            choose.pop()
            visit[i] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))
visit = [0] * N
arr.sort()
choose_list = []
choose = []

perm(0, M)
for c in choose_list:
    print(*c)