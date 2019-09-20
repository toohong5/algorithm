import sys
sys.stdin = open('n_m2.txt', 'r')

N, M = map(int, input().split())

choose = []
def comb(k, s):
    if k == M:
        choose.sort()
        print(*choose)
        return
    for i in range(s, N + 1):
        choose.append(i)
        comb(k + 1, i + 1)
        choose.pop()

comb(0, 1)