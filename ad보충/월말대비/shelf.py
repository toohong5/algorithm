import sys
sys.stdin = open('shelf.txt', 'r')

def comb(sum, n):
    global min_height
    if sum >= B:
        min_height = min(sum, min_height)
        return
    for i in range(n, N):
        comb(sum + heights[i], i + 1)
T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    min_height = 500000
    comb(0, 0)
    print('#{} {}'.format(tc, min_height - B))