import sys
sys.stdin = open('lotto.txt', 'r')

while True:
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    if n == 0:
        break
    else:
        choose = []
        def comb(k, s):
            if k == 6:
                print(*choose)
            for i in range(s, n):
                choose.append(arr[i])
                comb(k + 1, i + 1)
                choose.pop()
        comb(0, 0)
    print()
