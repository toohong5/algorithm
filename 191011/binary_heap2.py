import sys
sys.stdin = open('5177.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N + 1)
    i = 1
    index = 0

    while i <= N:
        tree[i] = arr[index]
        j = i
        while j//2 > 0:
            if tree[j//2] > tree[j]:
                tree[j//2], tree[j] = tree[j], tree[j//2]
            j = j//2
        i += 1
        index += 1

    sum = 0
    k = len(tree) - 1
    while k != 0:
        k = k // 2
        sum += tree[k]
    print('#{} {}'.format(tc, sum))
