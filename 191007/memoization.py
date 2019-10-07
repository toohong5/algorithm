def fibo(n):
    global cnt
    cnt += 1
    if n >= 2 and memo[n] == -1: # 한 번도 호출 안된 경우만 if문 수행
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n] # 리스트의 인덱스값 호출

N = int(input())
cnt = 0
memo = [-1] * (N + 1) # -1 이면 한번도 호출 안된 경우임..
memo[0] = 0
memo[1] = 1

print('피보나치 결과: ', fibo(N))
print(memo)
print('호출 횟수: ', cnt)

# ------------  반복이용 -------------------------------------

def fibo(n):
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]
N = int(input())
memo = [-1] * (N+1)
print('피보나치 결과: ', fibo(N))
print(memo)