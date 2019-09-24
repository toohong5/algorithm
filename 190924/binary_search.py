import sys
sys.stdin = open('bin.txt', 'r')

def binary(num, start, end):
    global count, result
    m = (start + end) // 2
    if start > end or m > end:
        return
    if num == a[m]:
        if '11' not in result and '22' not in result:
            count += 1
        elif result == '1' or result == '2':
            count += 1
        elif result == '':
            count += 1
        return
    elif num > a[m]:
        start = m + 1
        result += '1'
        binary(num, start, end)
    elif num < a[m]:
        end = m - 1
        result += '2'
        binary(num, start, end)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    count = 0
    for num in b:
        result = ''
        binary(num, 0, N - 1)
        print(result)
    print('#{} {}'.format(tc, count))