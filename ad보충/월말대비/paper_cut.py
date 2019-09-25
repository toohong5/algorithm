import sys
sys.stdin = open('paper_cut.txt', 'r')

N, M = map(int, input().split())
num = int(input())
for _ in range(num):
    rc, n = map(int, input().split())
       