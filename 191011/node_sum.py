# 노드의 개수 = n, n보다 큰 왼쪽 자식은 있을 수 없음.
# 트리 높이, 규칙
# 단말노드 위치에 값 넣고 부모노드에 값 채우기..

import sys
sys.stdin = open('5178.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n, m, l = map(int, input().split())
    arr = [0] * (n+1)
    for _ in range(m):
        li = list(map(int, input().split()))
        arr[li[0]] = li[1]
    if n % 2 != 0:
        for i in range(len(arr) - 1, 1, -2):
            if arr[(i - 1)//2] == 0:
                arr[(i - 1)//2] = arr[i - 1] + arr[i]
    else:
        arr[(len(arr)-1)//2] = arr[-1]
        for i in range(len(arr) - 2, 1, -2):
            if arr[(i - 1)//2] == 0:
                arr[(i - 1)//2] = arr[i - 1] + arr[i]
    print('#{} {}'.format(tc, arr[l]))