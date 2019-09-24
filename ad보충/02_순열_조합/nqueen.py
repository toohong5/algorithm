import sys
sys.stdin = open('nqueen.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visit = [0] * N
    count = 0
    cols = [0] * N
    
    arr = [[0] * N for _ in range(N)]