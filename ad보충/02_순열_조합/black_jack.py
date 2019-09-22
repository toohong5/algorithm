import sys
sys.stdin = open('black_jack.txt', 'r')

N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum_list = []
choose = []
def comb(k, s):
    if k == 3:
        if sum(choose) <= M:
            sum_list.append(sum(choose))
        return
    for i in range(s, N):
        choose.append(arr[i])
        comb(k + 1, i + 1)
        choose.pop()
comb(0, 0)
print(max(sum_list))