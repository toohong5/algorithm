import sys
sys.stdin = open('swimming_pool.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    fees = list(map(int, input().split()))
    month = list(map(int, input().split()))