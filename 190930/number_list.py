import sys
sys.stdin = open('number_list.txt', 'r')

def DFS(x, y, w, count):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    w += arr[x][y]
    if count == 6:
        w_set.add(w)
        return
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < 4 and 0 <= y1 < 4:
            DFS(x1, y1, w, count + 1)

T = int(input())
for tc in range(1, T + 1):
    arr = [list(input().split()) for _ in range(4)]
    visit = [[0] * 4 for _ in range(4)]
    w_set = set()
    for i in range(4):
        for j in range(4):
            if not visit[i][j]:
                visit[i][j] = 1
                w = ''
                DFS(i, j, w, 0)
    print('#{} {}'.format(tc, len(w_set)))