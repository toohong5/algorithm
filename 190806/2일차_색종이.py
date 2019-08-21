import sys
sys.stdin = open('input2_8.txt', 'r')

n = int(input())
arr = [[0] * 101 for _ in range(101)]
for i in range(1, n + 1):
    count = 0
    box = list(map(int, input().split()))
    for p in range(box[0], box[2] + 1):
        for q in range(box[1], box[3] + 1):
            if arr[p][q] == 0:
                arr[p][q] = i
            elif arr[p][q] != 0 and arr[p][q] != i:
                arr[p][q] = i
    else:
        for k in range(101):
            count += arr[k].count(i)
    print(count)

    # print(arr[i-1].count(i))

    
