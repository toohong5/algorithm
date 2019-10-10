import sys
sys.stdin = open('people_moving.txt', 'r')

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _  in range(n)]
print(arr)