# 두 그룹으로 나누기
# 모든 부분집합을 생성하면 두 그룹으로 나눌 수 있다!
arr = [10, 20, 30]
N = 3

for s in range(1 << N): # 0 ~ 2^n - 1
    A, B = [], []
    for i in range(N):
        if s & (1 << i):
            A.append(arr[i])
        else:
            B.append(arr[i])
    # print(A, B)

# 재귀호출
n = 3
def subset(k):
    if k == N + 1:
        print(a, b)
    else:
        a.append(k)
        subset(k + 1)   # k 번째 원소를 a에 포함(부분 집합 포함하는 선택)
        a.pop() # 원상복구

        b.append(k)
        subset(k + 1)   # k 번째 원소를 b에 포함(부분집합에 포함하지 않는 선택)
        b.pop()
a, b = [], []
subset(0)
