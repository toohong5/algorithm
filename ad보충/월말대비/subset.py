import sys
sys.stdin = open('subset.txt', 'r')

def comb(k, s):
    global count
    if k == N:
        return
    if sum(choose) == K:
        count += 1
        return
    for i in range(s, N):
        choose.append(arr[i])
        comb(k + 1, i + 1)
        choose.pop()

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    choose = []
    comb(0, 0)
    print(count)