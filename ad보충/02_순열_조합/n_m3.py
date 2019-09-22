import sys
sys.stdin = open('n_m2.txt', 'r')

N, M = map(int, input().split())
choose = []

def perm(k, s):
    if k == M:
        print(*choose)
        return
    for i in range(s, N + 1):
        choose.append(i)
        perm(k + 1, s)
        choose.pop()
perm(0, 1)
# for i in range(1, N):
#     for j in range(1, N):
#         print(i, j)
