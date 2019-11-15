import sys
sys.stdin = open('dessert.txt', 'r')

# def dfs(x, y, idx, order):
#     global maximum
#     if idx > 3:
#         return
#     x1 = x + dx[idx]
#     y1 = y + dy[idx]

#     if  0 <= x1 < n and 0 <= y1 < n:
#         if x1 == i and y1 == j:
#             if len(order) > maximum:
#                 maximum = len(order)
#                 return
#         if arr[x1][y1] in order:
#             return
#         order.append(arr[x1][y1])
#         dfs(x1, y1, idx, order)
#         dfs(x1, y1, idx + 1, order)
#         order.pop()



def cafe(x, y, idx, nums):
    global maximum
    if idx > 3:
        return
    x1 = x + dx[idx]
    y1 = y + dy[idx]
    if 0 <= x1 < n and 0 <= y1 < n:
        if x1 == i and y1 == j:
            if maximum < len(nums):
                maximum = len(nums)
                return
        if arr[x1][y1] not in nums:
            nums.append(arr[x1][y1])
            cafe(x1, y1, idx, nums)
            cafe(x1, y1, idx + 1, nums)
            nums.pop()

dx = [1, -1, -1, 1]
dy = [1, 1, -1, -1]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    maximum = 0
    for i in range(n):
        for j in range(n):
            cafe(i, j, 0, [arr[i][j]])
    if maximum == 0:
        maximum = -1
    print('#{} {}'.format(tc, maximum))