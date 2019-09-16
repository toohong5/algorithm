# 조합
arr = 'abcde'
n = len(arr)
for i in range(n): # 남길개수만큼 남기는게 좋긴함... n -> n-2 (적어도 2개 남겨야함)
    for j in range(i + 1, n): # 첫번째꺼 다음것 부터!! / n -> n-1(1개 남겨야함)
        for k in range(j + 1, n):
            print(arr[i], arr[j], arr[k])

# 중복조합(nHr)
arr = 'abcde'
n = len(arr)
for i in range(n):
    for j in range(i, n): # 첫번째꺼 다음것 부터!!
        for k in range(j, n):
            print(arr[i], arr[j], arr[k])

# 재귀
def nCr(n, r):
    if n == r or r == 0: return 1
    else:
        return nCr(n-1, r-1) + nCr(n-1, r)
        # n개의 원소 중 r개를 뽑는데 특정 원소 하나를 포함시킨 경우와 포함시키지 않은 경우를 더한다.
print(nCr(5, 3))
print(nCr(30, 15))

# 부분집합 조합
def comb(k, s):
    if k == r: # r개 뽑으면 출력
        print(choose)
    else:
        for i in range(s, n):
            choose.append(arr[i])
            comb(k + 1, i + 1)
            choose.pop()
comb(0, 0)

arr = 'abcde'
n, r = len(arr) , 3
choose = []
for i in range(n): # 남길개수만큼 남기는게 좋긴함... n -> n-2 (적어도 2개 남겨야함)
    choose.append(arr[i])
    for j in range(i + 1, n): # 첫번째꺼 다음것 부터!! / n -> n-1(1개 남겨야함)
        choose.append(arr[j])
        for k in range(j + 1, n):
            choose.append(arr[k])
            print(choose)
            choose.pop()
        choose.pop()
    choose.pop()
