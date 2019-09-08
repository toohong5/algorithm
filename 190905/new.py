import sys
sys.stdin = open('input3.txt', 'r')

T = int(input())
for tc in range(1):
    p, q  = map(int, input().split())
    arr = [[0] * 301 for _ in range(301)]

    arr[1][1] = (1,1)
    x = 0
    y = 0
    while x < len(arr):
        arr[x][y].append((x, y))
        x -= 1
        y += 1
    # for i in range(302):
    #     for j in range(302):
    #         arr[i][0] = (1, i+1)
            
    #         while len(arr[i-1]) != i:
    #             arr[i][j] = (j, i)
    # for i in range(51, 101):
    #     for j in range(1, 101):
            
#--------------------------------------------------------------------------------
