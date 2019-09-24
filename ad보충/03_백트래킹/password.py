import sys
sys.stdin = open('password.txt', 'r')

def comb(k, n):
    if k == N:
        count = 0
        for c in choose:
            if c in vowels:
                count += 1
        if 1 <= count <= N - 2:
            result = ''.join(choose)
            print(result)
        return
    for i in range(n, M):
        if not visit[i]:
            visit[i] = 1
            choose.append(arr[i])
            comb(k + 1, i)
            choose.pop()
            visit[i] = 0

N, M = map(int, input().split())
arr = list(input().split())
arr.sort()
vowels = 'aeiou'
choose = []
result_list = []
visit = [0] * M
comb(0, 0)