import sys
sys.stdin = open('password.txt', 'r')
def perm(k, n):
    if k == N:
        a = choose[::]
        count = 0
        for c in a:
            if c in vowels:
                count += 1
        if 1 <= count <= N - 2:
            a.sort()
            result = ''.join(a)
            result_list.add(result)
        return
    for i in range(n, M):
        if not visit[i]:
            visit[i] = 1
            choose.append(arr[i])
            perm(k + 1, n)
            choose.pop()
            visit[i] = 0

N, M = map(int, input().split())
arr = list(input().split())
arr.sort()
vowels = 'aeiou'
choose = []
result_list = set()
visit = [0] * M
perm(0, 0)
for i in sorted(list(result_list)):
    print(i)
