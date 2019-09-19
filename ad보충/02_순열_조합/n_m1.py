import sys
sys.stdin = open('n_m1.txt', 'r')

n, m = map(int, input().split())
visit = [0] * (n + 1)
choose = []
def perm(k, n):
    if k == m:
        # choose.sort()
        print(*choose)
        return
    for i in range(1, n+1):
        if visit[i]:continue
        visit[i] = 1
        choose.append(i)
        perm(k + 1, n)
        choose.pop()
        visit[i] = 0
perm(0, n)

# arr = [i for i in range(1, n + 1)]
# result = []
# for i in range(1 << len(arr)):
#     a = []
#     for j in range(len(arr)):
#         if i & 1 << j:
#             a.append(arr[j])
#     if len(a) == m:
#         result.append(a)
# print(*result)


# for i in range(1, n+1):
