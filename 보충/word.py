import sys
sys.stdin = open('word_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    # 1: white, 0: black
    arr = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1: # 행
                for k in range(c, c + K):
                    