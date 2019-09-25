import sys
sys.stdin = open('bus2.txt', 'r')

def charge(battery, count, i):
    global min_count
    if count > min_count:
        return
    if i == N - 1:
        min_count = min(count, min_count)
        return
    if battery == 0:
        charge(arr[i] - 1, count + 1, i + 1)
    else:
        charge(battery - 1, count, i + 1)
        charge(arr[i] - 1, count + 1, i + 1)

T = int(input())
for tc in range(1, T + 1):
    N, *arr = map(int, input().split())
    min_count = 5000000
    charge(arr[0], 0, 0)

    print('#{} {}'.format(tc, min_count))