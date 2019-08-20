import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    for i in range(n):
        sum = 0
        for j in range(n):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
            sum = sum + row_sum + col_sum - arr[]