import sys
sys.stdin = open('honey.txt', 'r')

def subset(array):
    maxi = 0
    for i in range(1 << len(array)):
        a = []
        for j in range(len(array)):
            if i & (1 << j):
                a.append(array[j])
        if sum(a) <= C:
            sum1 = 0
            for i in range(len(a)):
                sum1 += a[i]**2
            if maxi < sum1:
                maxi = sum1
    return maxi

T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    result = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            if subset(honey[i][j:j + M]) not in result:
                result[i].append(subset(honey[i][j:j + M]))
    maximum = 0
    for idx, i in enumerate(result):
        if maximum < max(i):
            maximum = max(i)
            x, y = idx, i.index(max(i))
    result[x][y] = 0
    for i in range(1, M):
        if 0 <= y-i < len(result[0]):
            result[x][y-i] = 0
        if 0 <= y + i < len(result[0]):
            result[x][y+i] = 0
    maximum2 = 0
    for idx, i in enumerate(result):
        if maximum2 < max(i):
            maximum2 = max(i)
    
    print('#{} {}'.format(tc, maximum + maximum2))