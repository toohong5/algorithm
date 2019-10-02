import sys
from pprint import pprint
sys.stdin = open('honey.txt', 'r')


def dfs(x, y, box):
    visit[x][y] = 1
    box.append(honey[x][y])
    if len(box) == M:
        
        result.append(box)
        box = [honey[x][y]]
    x1, y1 = x, y + 1
    if 0 <= x1 < N and 0 <= y1 < N:
        if not visit[x1][y1]:
            dfs(x1, y1, box)
    else:
        return

T = int(input())
for tc in range(1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    
    visit = [[0] * N for _ in range(N)]

    result = []
    for i in range(N):
        for j in range(N):
            box = []
            dfs(i, j, box)
    print(result)