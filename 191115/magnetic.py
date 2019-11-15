import sys
sys.stdin = open('magnetic.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    k = int(input())
    arr = [list(map(int, input().split())) for _ in range(4)]
    for i in range(k):
        mag, rotate = map(int, input().split())  
        for j in range(len(arr)):
            if rotate == 1:
                arr[mag][j] = 