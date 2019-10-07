def fibo(n):
    global cnt
    cnt += 1
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

N = int(input())
cnt = 0
print('피보나치 결과:', fibo(N))
print('호출 횟수:', cnt)