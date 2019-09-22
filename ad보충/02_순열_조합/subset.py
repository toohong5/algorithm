import sys
sys.stdin = open('subset.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    count = 0
    for i in range(1 << len(arr)):
        a = []
        for j in range(len(arr)):
            if i & 1<<j:
                a.append(arr[j])
        if sum(a) == M:
            count += 1
    print('#{} {}'.format(tc, count))