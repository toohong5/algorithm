import sys
sys.stdin = open('input3.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    p, q  = map(int, input().split())
    arr = [[0] * 101 for _ in range(101)]

    for i in range(51):
        for j in range(101):
            arr[i][0] = (1, i+1)
            
            while len(arr[i-1]) != i:
                arr[i][j] = (j, i)
    for i in range(51, 101):
        for j in range(1, 101):
            
