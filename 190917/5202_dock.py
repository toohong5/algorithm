import sys
sys.stdin = open('dock.txt', 'r')

# def delete(start, row):
#     if start == row:
#         return 1
#     for i in range(row, len(arr)):
#         if start[1] > arr[i][0]:
#             arr.pop(i)
#             delete(arr[i], i)
# for i in range(1, N):
#     if result[-1][1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key = lambda x:x[1])
    for s in range(len(arr)):
        start = arr[s]
        if arr[s] != [0, 0]:
            for i in range(s + 1, len(arr)):
                if start[1] > arr[i][0]:
                    arr[i] = [0, 0]
    count = 0
    for row in arr:
        if sum(row) != 0:
            count += 1
    print('#{} {}'.format(tc, count))