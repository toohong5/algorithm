import sys
sys.stdin = open('nqueen.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    