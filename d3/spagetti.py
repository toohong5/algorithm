import sys
sys.stdin = open('spagetti.txt','r')

T = int(input().split())
for tc in range(1, T + 1):
    N, B, E = map(int, input().split())
    time = list(map(int, input().split()))

    result = 0
    if sum(time) >= (B + E):
        result = 0
    else:
        U = (B+E) - sum(time)
        L = (B-E) - sum(time)
        
