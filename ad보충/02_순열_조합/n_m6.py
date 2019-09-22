import sys
sys.stdin = open('n_m5.txt', 'r')

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

choose = []
def comb(k, s):
    if k == M:
        print(*choose)
        return
    for i in range(s, N):
        choose.append(arr[i])
        comb(k + 1, i + 1)
        choose.pop()
comb(0, 0)