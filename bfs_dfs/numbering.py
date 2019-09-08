import sys
sys.stdin = open('numbering.txt', 'r')

def BFS(x, y, count):
    visit = [[0] * N for _ in range(N)]
    
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

result = 0
x = y = 0
count = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            x = i
            y = j
            result += BFS(x, y, count)