# 중복순열
arr = 'abc'
n = len(arr)
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(arr[i], arr[j], arr[k])

# 순열
arr = 'abc'
n = len(arr)
for i in range(n):
    for j in range(n):
        if j == i: continue
        for k in range(n):
            if k==i or k == j: continue
            print(arr[i], arr[j], arr[k])

# 부분집합 순열 재귀
S = []
def perm(k, n): # k: 시작점, n: 끝점
    if k == n:
        print(arr)
    else:
        for row in arr:
            for i in range(k, n):
                row[k], row[i] = row[i], row[k] # 1번 위치 기준으로 자리바꿔감..
                perm(k + 1, n)
                row[k], row[i] = row[i], row[k]

arr = [1, 2, 3, 4]
n = len(arr)
for i in range(n):
    arr[0], arr[i] = arr[i], arr[0] # 자리바꾸고
    for j in range(1, n):
        arr[1], arr[j] = arr[j], arr[1] # 1번 위치 기준으로 자리바꿔감..
        for k in range(2, n):
            arr[2], arr[k] = arr[k], arr[2] # 1번 위치 기준으로 자리바꿔감..
            print(arr)
            arr[2], arr[k] = arr[k], arr[2]
        arr[1], arr[j] = arr[j], arr[1]
    arr[0], arr[i] = arr[i], arr[0] # 다시 복구