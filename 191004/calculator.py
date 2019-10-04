import sys
sys.stdin = open('calculator.txt', 'r')

def subset(array):
    result = []
    for i in range(1 << len(array)):
        a = []
        for j in range(len(array)):
            if i & (1 << j):
                a.append(array[j])
        if len(a) != 0:
            b = ''.join(a)
            result.append(int(b))    
    return result

def count(x, cnt, i):
    global X
    for i in range(len(result)):
        if result[i] in divisors:
            if X % result[i] == 0:
                cnt += 1
                return
            else:
                count(X // result[i], cnt + 1, i + 1)

T = int(input())
for tc in range(1):
    arr = list(map(int, input().split()))
    X = int(input())
    num = []
    divisors = []
    for i in range(len(arr)):
        if arr[i] == 1:
            num.append(str(i))
    for i in range(1, X + 1):
        if X % i == 0:
            divisors.append(i)
    result = subset(num)
    divisors.sort(reverse=True)
    total = []
    for divisor in divisors:
        if divisor in result:
            count(divisor, 0, result.index(divisor))