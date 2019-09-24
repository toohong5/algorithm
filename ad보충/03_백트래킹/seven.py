import sys
sys.stdin = open('seven.txt', 'r')

def DFS(x, y, count):
    global result
    if count == 7:
        result += 1
        return
    

arr = [list(input()) for _ in range(5)]
# s가 4개 이상
# 7명 자리 인접
result = 0
for i in range(N):
    for j in range(N):
        DFS(i, j, 0)