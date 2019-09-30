import sys
from pprint import pprint
sys.stdin = open('best_route.txt', 'r')



# def DFS(x, y, s, count):
#     if s > min_sum:
#         return
#     if count == N:
#         min_sum = min(s + abs(x - xy_list[1][0]) + abs(y - xy_list[1][1]), min_sum)
#         return
#     for i in range(2, N + 1):
#         x = xy_list[i][0]
#         y = xy_list[i][1]

def perm(k, n, x, y, sum1):
    global min_sum
    if sum1 >= min_sum:
        return
    if k == n:
        idx = choose[-1]
        min_sum = min(sum1 + abs(xy_list[idx][0] - xy_list[-1][0]) + abs(xy_list[idx][1] - xy_list[-1][1]), min_sum)
        return
    for i in range(1, N + 1):
        if not visit[i]:
            visit[i] = 1
            choose.append(i)
            perm(k + 1, n, xy_list[i][0], xy_list[i][1], sum1 + abs(x - xy_list[i][0]) + abs(y - xy_list[i][1]))
            visit[i] = 0
            choose.pop()

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 고객의 수
    arr = list(map(int, input().split()))
    xy_list = []
    choose = []
    min_sum = 50000000
    visit = [0] * (N + 2)
    for i in range(0, len(arr) - 1, 2):
        x = arr[i]
        y = arr[i + 1]
        xy_list.append([x, y])
    p = xy_list.pop(1)
    xy_list.append(p)
    perm(0, N, xy_list[0][0], xy_list[0][1], 0)
    print('#{} {}'.format(tc, min_sum))