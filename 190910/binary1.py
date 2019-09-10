import sys
sys.stdin = open('input3.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, HEXA = input().split()
    N = int(N)
    
    result = ''
    b = 0
    for h in HEXA:
        b = bin(int(h, 16))
        b = b[2:]
        while len(b) != 4:
            b = '0' + b
        result += b
    print('#{} {}'.format(tc, result))