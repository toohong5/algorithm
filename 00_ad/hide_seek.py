import sys
sys.stdin = open('hide_seek.txt', 'r')
from collections import deque

def BFS(n, cnt):
    q = deque()
    q.append((n, cnt))
    while q:
        num, count = q.popleft()
        if n == K:
            min_count = min(cnt, min_count)
            return
        if min_count < cnt:
            return
        for i in range(3):
            if i == 0:
                num = num + 1
                if 0 <= num <= 100000:
                    q.append 
N, K = map(int, input().split())
min_count = 5000000
