import sys
sys.stdin = open('merge.txt', 'r')
# 리스트를 사용해서 append, pop, 슬라이싱 쓰면 --> 시간초과!!!
# 연결리스트, 배열처럼 만들면 가능..
def mergeSort(lo, hi):
    global count
    if lo == hi:
        return
    mid = (lo + hi - 1) // 2
    mergeSort(lo, mid)
    mergeSort(mid + 1, hi)

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
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0
    tmp = [0] * len(arr)
    print(arr)
    mergeSort(0, len(arr) - 1)
    print('#{} {} {}'.format(tc, arr[N//2], count))
    # print(arr)
    # print(tmp)



# -------------- 꼼수 -----------------------
def merge(lo, hi):
    global ans
    if lo + 1 == hi:
        return arr[lo]
    mid = (lo + hi) // 2
    l = merge(lo, mid)
    r = merge(mid, hi)
    
    if l > r:
        ans += 1
        return l
    else:
        return r

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    merge(0, N)
    arr.sort()
    print('#{} {} {}'.format(tc, arr[N//2], ans))