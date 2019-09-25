import sys
sys.stdin = open('paper.txt', 'r')

N = int(input())
arr = [[0] * 101 for _ in range(101)]

for k in range(1, N + 1):
    box = list(map(int, input().split()))
    for i in range(box[0], box[0] + box[2]):
        for j in range(box[1], box[1] + box[3]):
            # if arr[i][j] == 0:
            #     arr[i][j] = k
            
            arr[i][j] = k
# count = 0
for k in range(1, N + 1):
    count = 0
    for i in range(101):
        for j in range(101):
            if arr[i][j] == k:
                count += 1
    print(count)
# print(count)