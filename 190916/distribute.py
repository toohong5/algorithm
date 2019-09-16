import sys
sys.stdin = open('input.txt', 'r')

def perm(per, row):
    

T = int(input())
for tc in range(1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] / 100



