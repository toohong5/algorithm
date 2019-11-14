import sys
sys.stdin = open('hide_seek.txt', 'r')
sys.setrecursionlimit(10**6)

def bfs(x, count):
    

def find(x, count):
    global min_count
    if x < 0 or x > 100000:
        return
    if x == k:
        min_count = min(min_count, count)
        return

    dx = [-1, 1, 2]
    for i in range(3):
        if i == 2:
            x1 = x * dx[i]
        else:
            x1 = x + dx[i]

        if 0<= x1 < 100000:
            find(x1, count + 1)
        # else:
            
        #     return

    # find(idx - 1, count + 1)
    # find(idx + 1, count + 1)
    # find(idx * 2, count + 1)

n, k = map(int, input().split())
min_count = 50000000
# print(n, k)
find(n, 0)
print(min_count)