arr = [69, 10, 30, 2, 16, 8, 31, 22]
tmp = [0] * len(arr)
def mergeSort(lo, hi): # 매개변수 -> 문제의 크기
    # print(lo, hi)
    if lo == hi: # lo 와 hi 가 같으면 return
        return
    # 분할()
    mid = (lo + hi) >> 1 # == (lo +hi) //2
    mergeSort(lo, mid) # 왼쪽(left), 가운데(mid)
    mergeSort(mid + 1, hi) # 가운데(mid+1), 오른쪽(right)
    # 왼쪽과 오른쪽 병합(merge)
    i, j, k = lo, mid + 1, lo 
    while i <= mid and j <= hi: # i는 mid까지 j는 hi 까지 간다(go)
        if arr[i] < arr[j]: # arr[j] 가 arr[i] 보다 클 때
            tmp[k] = arr[i] # tmp[k]를 arr[i]로 바꾼다.
            i, k = i + 1, k + 1 # i를 1 증가시키고 k를 1증가시킨다.
        else:
            tmp[k] = arr[j] # arr[j] 가 arr[i] 보다 작을 때
            j, k = j + 1, k + 1 # j 를 1 증가시키고 k 를 1 증가시킨다.
    while i <= mid: # i 는 mid 보다 작거나 같을 때 실행
        tmp[k] = arr[i] # tmp[k]를 arr[i]로 바꾼다.
        i, k = i + 1, k + 1 # i를 1 증가시키고 k를 1증가시킨다.
    while j <= hi: # j 는 mid 보다 작거나 같을 때 실행
        tmp[k] = arr[j] # tmp[k]를 arr[j]로 바꾼다.
        j, k = j + 1, k + 1 # j 를 1 증가시키고 k 를 1 증가시킨다.
    for i in range(lo, hi + 1): 
        arr[i] = tmp[i]
    print(tmp)
    print()
    print(arr)
# print(arr)        
mergeSort(0, len(arr)-1)
# print(arr)