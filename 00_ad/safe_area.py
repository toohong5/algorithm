import sys
sys.stdin = open('safe_area.txt', 'r')
from collections import deque

def BFS(x, y, cnt, height):
    global count
    q = deque()
    q.append([x, y, cnt])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

heights = []
for i in range(N):
    for j in range(N):
        if arr[i][j] not in heights:
            heights.append(arr[i][j])
            BFS(0, 0, 0, arr[i][j])
min_height = 50000
for row in arr:
    if min_height > min(row):
        min_height = min(row)

count = 0
BFS(0, 0, 0, min_height)