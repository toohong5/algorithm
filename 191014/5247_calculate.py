import sys
sys.stdin = open('5247.txt', 'r')

def calculate(num, cnt):
    global count
    if count <= cnt:
        return
    if num <= 0 or num > 1000000:
        return
    if num == m:
        count = min(count, cnt)
        return
    elif num < m:
        if abs((num * 2) - m) > abs(num + 1 - m):
            calculate(num + 1, cnt + 1)
        else:
            calculate(num * 2, cnt + 1)
    elif num > m:
        if abs(num - 2 - m) > abs(num - 10 - m):
            calculate(num - 10, cnt + 1)
        else:
            calculate(num - 1, cnt + 1)

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    count = 100000000000
    calculate(n, 0)
    print('#{} {}'.format(tc, count))