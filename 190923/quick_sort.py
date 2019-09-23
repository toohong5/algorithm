arr = [69, 10, 30, 2, 16, 8, 31, 22]
def quickSort(lo, hi):
    if lo >= hi:
        return
    i, j, pivot = lo, hi, arr[lo]
    while i < j:
        while i <= hi and pivot >= arr[i]:  i += 1
        while pivot < arr[j]: j -= 1    # pivot과 같으면 j 멈춤!!
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]
    quickSort(lo, j - 1)
    quickSort(hi, j - 1)

print(arr)
quickSort(0, len(arr) - 1)
print(arr)

#--------- 삽입정렬이용 ---------------------

arr = [69, 10, 30, 2, 16, 8, 31, 22]
def quickSort(lo, hi):
    if lo >= hi:
        return
    i = lo - 1
    for j in range(lo, hi): # 시작위치 ~ 마지막 전까지..
        if arr[hi] >= arr[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[hi], arr[i] = arr[i], arr[hi] # i 다음 위치 애랑 pivot 바꾸기 

    quickSort(lo, i - 1)
    quickSort(i + 1, hi)

print(arr)
quickSort(0, len(arr) - 1)
print(arr)