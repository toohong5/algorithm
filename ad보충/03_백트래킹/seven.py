import sys
sys.stdin = open('seven.txt', 'r')

def DFS(x, y, count, w):
    global result
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    w += arr[x][y]
    if w.count('Y') > 3:
        return
    if count == 7:
        if w.count('S') >= 4:
            w_list.add(w)
        return
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < 5 and 0 <= y1 < 5:
            DFS(x1, y1, count + 1, w)
    
arr = [list(input()) for _ in range(5)]
visit = [[0] * 5 for _ in range(5)]
# s가 4개 이상
# 7명 자리 인접
result = 0
w_list = set()
for i in range(5):
    for j in range(5):
        if not visit[i][j]:
            visit[i][j] = 1
            w = ''
            DFS(i, j, 1, w)

print(len(w_list))