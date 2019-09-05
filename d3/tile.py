import sys
import math
sys.stdin = open('tile.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, A, B = map(int, input().split())
    min = 10000000000000000
    R = C = 0
    for r in range(N):
        for c in range(1, int(N**0.5) + 2):
            if r*c > N:
                break
            elif (A * abs(r - c) + B * (N - r * c)) < min:
                min = (A * abs(r - c) + B * (N - r * c))
                R = r
                C = c
    print(R, C)
    print('#{} {}'.format(tc, min))

