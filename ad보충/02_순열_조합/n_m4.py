import sys
sys.stdin = open('n_m2.txt', 'r')

# def comb(e, n):
#     global result
#     if n == nums:
#         q = sorted(result)
#         if q not in a:
#             a.append(q)
#             print(*q)
#         return
#     else:
#         for i in range(1, num+1):
#             result.append(i)
#             comb(e+1, n+1)
#             result.pop()
    
# num, nums = map(int, input().split())
# a = []
# result = []
# comb(1, 0)




N, M = map(int, input().split())
choose = []

def perm(k, s):
    if k == M:
        print(*choose)
        return
    for i in range(s, N + 1):
        if len(choose) == 0:
            choose.append(i)
            perm(k + 1, s)
            choose.pop()
        elif i >= choose[-1]:
            choose.append(i)
            perm(k + 1, s)
            choose.pop()
perm(0, 1)