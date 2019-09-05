import sys
sys.stdin = open('calculator.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    S = []
    max = 0

    while len(num) != 1:
        n1 = num.pop(0)
        n2 = num.pop(0)
        if n1 + n2 >= n1 * n2:
            num.insert(0, (n1 + n2))
        else:
            num.insert(0, (n1 * n2))
    print('#{} {}'.format(tc, num[0]))