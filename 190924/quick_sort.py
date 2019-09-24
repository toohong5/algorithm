import sys
sys.stdin = open('quick.txt', 'r')

def quick(lo, hi):
    if lo >= hi:
        return
    i = lo - 1
    for j in range(lo, hi):
        if arr[hi] >= arr[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[hi], arr[i] = arr[i], arr[hi]

    quick(lo, i - 1)
    quick(i + 1, hi)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick(0, len(arr) - 1)
    print('#{} {}'.format(tc, arr[N//2]))