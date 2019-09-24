import sys
sys.stdin = open('jump.txt', 'r')

def DFS(x, y, count, w):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if count == 6:
        if w not in w_list:
            w_list.append(w)
        return
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < 5 and 0 <= y1 < 5:
            DFS(x1, y1, count+1, w + arr[x1][y1])

arr = [list(input().split()) for _ in range(5)]
visit = [[0] * 5 for _ in range(5)]
w_list = []
for i in range(5):
    for j in range(5):
        if not visit[i][j]:
            w = ''
            visit[i][j] = 1
            DFS(i, j, 0, w)

print(len(w_list))