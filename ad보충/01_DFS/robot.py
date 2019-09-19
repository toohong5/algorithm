import sys
sys.stdin = open('robot.txt', 'r')

def DFS(x, y, per, count):
    global E, W, S, N
    global prob
    if count == 0:
        prob += per
        return
    for i in range(4):
        if way[i] == 'E':
            x1 = x 
            y1 = y + 1
            if not visit[x1][y1]:
                visit[x1][y1] = 1
                DFS(x1, y1, per*E, count - 1)
                visit[x1][y1] = 0
        elif way[i] == 'W':
            x1 = x 
            y1 = y - 1
            if not visit[x1][y1]:
                visit[x1][y1] = 1
                DFS(x1, y1, per*E, count - 1)
                visit[x1][y1] = 0
        elif way[i] == 'S':
            x1 = x + 1
            y1 = y
            if not visit[x1][y1]:
                visit[x1][y1] = 1
                DFS(x1, y1, per*E, count - 1)
                visit[x1][y1] = 0
        elif way[i] == 'N':
            x1 = x - 1
            y1 = y
            if not visit[x1][y1]:
                visit[x1][y1] = 1
                DFS(x1, y1, per*E, count - 1)
                visit[x1][y1] = 0

M, E, W, S, N = map(int, input().split())
E, W, S, N = E/100, W/100, S/100, N/100
way = ['E', 'W', 'S', 'N']
visit = [[0] * 29 for _ in range(29)]
visit[14][14] = 1
prob = 0
DFS(14, 14, 1, M)
print(prob)