import sys
sys.stdin = open('input3.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, HEXA = input().split()
    N = int(N)
    print(N, HEXA)
