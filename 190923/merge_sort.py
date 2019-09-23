import sys
sys.stdin = open('merge.txt', 'r')

def mergeSort(lo, hi):
    global count
    if lo == hi:
        return
    mid = (lo + hi - 1) // 2
    mergeSort(lo, mid)
    mergeSort(mid + 1, hi)
    print(arr[lo:mid])
    print(arr[mid:hi])

    if arr[mid] > arr[hi]:
        count += 1
    i, j, k = lo, mid + 1, lo
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i, k = i + 1, k + 1
        else:
            tmp[k] = arr[j]
            # count += 1
            j, k = j + 1, k + 1
    while i <= mid:
        tmp[k] = arr[i]
        i, k = i + 1, k + 1
    while j <= hi:
        tmp[k] = arr[j]
        j, k = j + 1, k + 1
    # print(tmp)

    for i in range(lo, hi + 1):
        arr[i] = tmp[i]
    # print(arr)
T = int(input())
for tc in range(1):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0
    tmp = [0] * len(arr)
    print(arr)
    mergeSort(0, len(arr) - 1)
    print(count, arr[N//2])
    # print(arr)
    # print(tmp)