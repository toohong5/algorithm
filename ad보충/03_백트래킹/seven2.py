import sys
sys.stdin = open('seven.txt', 'r')

def comb(k, s, x, y, w, count):
    if w.count('Y') > 3:
        return
    if count == 7:
        if w.count('S') >= 4:
            pass
        return
    for i in range(s, N):
        w += arr[]
arr = [list(input()) for _ in range(5)]
# 좌표랑 같이 comb만들어서..dfs로 연결 확인하기..
