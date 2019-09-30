import sys
from pprint import pprint
sys.stdin = open('best_route.txt', 'r')

def min_dis(dis, row, count):
    global min_distance
    if dis > min_distance:
        return
    if count == N + 2:
        # dis += distance[row][N + 1]
        min_distance = min(dis, min_distance)
        return
    for i in range(1, N + 2):
        if i == N + 1:
            if count == N + 1:
                min_dis(dis + distance[row][i], i, count + 1)
        else:
            if not visit[i]:
                if row != i:
                    visit[i] = 1
                    min_dis(dis + distance[row][i], i, count + 1)
                    visit[i] = 0

T = int(input())
for tc in range(1):
    N = int(input()) # 고객의 수
    arr = list(map(int, input().split()))
    xy_list = []
    visit = [0] * (N + 2)
    # distance = [[0] * (N + 2) for _ in range(N + 2)]
    min_distance = 50000000000
    for i in range(0, len(arr) - 1, 2):
        x = arr[i]
        y = arr[i + 1]
        xy_list.append([x, y])
    print(xy_list)
    # p = xy_list.pop(1)
    # xy_list.append(p)
    # for i in range(N + 2):
    #     for j in range(N + 2):
    #         distance[i][j] = abs(xy_list[i][0] - xy_list[j][0]) + abs(xy_list[i][1] - xy_list[j][1])
    visit[0] = 1
    # min_dis(0, 0, 0)
    # print('#{} {}'.format(tc, min_distance))
    # pprint(distance)