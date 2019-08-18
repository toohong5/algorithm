import sys
sys.stdin('input2_7.txt', 'r')

n = int(input())
for tc in range(1, n+1):
    x, y, dx, dy = map(int, input().split())
    x2, y2, dx2, dy2 = map(int, input().split())

    box1 = [[0] * dx for i in range(dx)]
    
