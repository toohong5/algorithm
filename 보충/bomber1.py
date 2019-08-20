import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    row = []
    col = []
    for i in range(n):
        row_sum = 0
        col_sum = 0
        for j in range(n):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        row.append(row_sum)
        col.append(col_sum)

    max_sum = 0
    r = c = 0
    for x in range(n):
        for y in range(n):
            total = 0
            total = row[x] + col[y] - arr[x][y]
            if max_sum < total:
                max_sum = total
                r = x
                c = y
            elif max_sum == total:
                r = x
                c = y
    
    print('#{} {} {} {}'.format(tc, r, c, max_sum))




    # max_sum = 0
    # r=0
    # c=0
    # for i in range(n):
    #     row_sum = 0
    #     col_sum = 0
    #     for j in range(n):
    #         sum = 0
    #         sub = 0
    #         row_sum += arr[i][j]
    #         for k in range(n):
    #             col_sum += arr[k][j]
    #             if arr[i][j] == arr[k][j]:
    #                 sub = arr[i][j]
    #         sum = sum + row_sum + col_sum - sub
    #         if sum > max_sum:
    #             max_sum = sum
    #             r = i
    #             c = j
    # print(sum)

