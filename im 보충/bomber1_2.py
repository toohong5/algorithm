import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    max_sum = 0
    row_sum = 0
    for i in range(n):
        row_sum = sum(arr[i])
        for j in range(n):
            col_sum = 0
            for k in range(n):
                col_sum += arr[k][j]
            total = row_sum + col_sum - arr[i][j]
            if total > max_sum:
                max_sum = total
    print('#{} {}'.format(tc, max_sum))