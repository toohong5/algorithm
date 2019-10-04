import sys
sys.stdin = open('swimming_pool.txt', 'r')

def fee(sum1, i):
    global min_sum
    if sum1 >= min_sum:
        return
    if i >= 12:
        min_sum = min(sum1, min_sum)
        return
    if month[i] != 0:
        fee(sum1 + (fees[0] * month[i]), i + 1)
        fee(sum1 + fees[1], i + 1)
        fee(sum1 + fees[2], i + 3)
    else:
        fee(sum1, i + 1)

T = int(input())
for tc in range(1, T + 1):
    fees = list(map(int, input().split()))
    month = list(map(int, input().split()))
    min_sum = fees[-1]
    fee(0, 0)
    print('#{} {}'.format(tc, min_sum))