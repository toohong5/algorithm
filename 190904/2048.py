import sys
sys.stdin = open('input5.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, way = input().split()
    N = int(N)
    arr = [list(map(int, input().split())) for _ in range(N)]

    if way == "up":
        