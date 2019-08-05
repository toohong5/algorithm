import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = []

# 100*100 배열 불러오기
for i in range(100):
    num = input().split()
    arr.append(num)


n, m = len(arr), len(arr[0])

# 행의 합
row_sum = []
sum1 = 0
max1 = 0
for i in range(n):
    for j in range(m):
        sum1 += int(arr[i][j])
    row_sum.append(sum1)
    sum1 = 0
print(row_sum)

# 열의 합
column_sum = []
sum2 = 0
max2 = 0
for i in range(n):
    for j in range(m):
        sum2 += int(arr[j][i])
    column_sum.append(sum2)
    sum2 = 0
print(column_sum)

# 우대각의 합
cross_sum1 = []
sum3 = 0
max3 = 0
for diag in range(0, n + m - 1):    # diag: 사선의 수
                                    # x, y: 시작 좌표
    x = 0 if diag < m else (diag - m + 1)
    y = diag if diag < m else m - 1

    while x < n and y >= 0:
        sum3 += int(arr[x][y])
        x += 1
        y -= 1
    cross_sum1.append(sum3)
    sum3 = 0
print(cross_sum1)

# 좌대각의 합
cross_sum2 = []
sum4 = 0
max4 = 0
for diag in range(0, n + m - 1):    # diag: 사선의 수
                                    # x, y: 시작 좌표
    x = 0 if diag < m else (diag - m + 1)
    y = diag if diag < m else m-1

    while x < n and y >= 0:
        sum4 += int(arr[y][x])
        x -= 1
        y += 1
    cross_sum2.append(sum4)
    sum4 = 0
print(cross_sum2)
