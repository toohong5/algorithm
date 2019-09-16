arr = [9, 2, 3, 7, 5, 6, 8, 1, 4, 10]

def getMin(start, end): # 최소값 구하기
    if start == end:    # 기저사례
        return arr[start]
    else:
        ret = getMin(start, end - 1)
        return min(ret, arr[end])

print(getMin(0, len(arr) - 1))

# 중간을 나눠서 구하기
def getMin(start, end): # 최소값 구하기
    if start == end:    # 기저사례
        return arr[start]
    else:
        mid = (start + end) // 2
        l = getMin(start, mid)
        r = getMin(mid + 1, end)
        return min(l, r)

print(getMin(0, len(arr) - 1))