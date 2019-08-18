import sys
sys.stdin = open('input5.txt', 'r')

print(dir(list))

N = int(input())
for k in range(1, N+1):
    nums = list(map(int, input().split()))

