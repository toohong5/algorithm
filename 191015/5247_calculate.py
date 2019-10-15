import sys
sys.stdin = open('5247.txt', 'r')

# def calculate(num, cnt):
#     global count
#     if count <= cnt:
#         return
#     if num <= 0 or num > 1000000:
#         return
#     if num == m:
#         count = min(count, cnt)
#         return
#     elif num < m:
#         if abs((num * 2) - m) > abs(num + 1 - m):
#             calculate(num + 1, cnt + 1)
#         else:
#             calculate(num * 2, cnt + 1)
#     elif num > m:
#         if abs(num - 2 - m) > abs(num - 10 - m):
#             calculate(num - 10, cnt + 1)
#         else:
#             calculate(num - 1, cnt + 1)

from collections import deque
def BFS(num, cnt):
    global count
    q = deque()
    q.append((num, cnt))
    visit[num] = 1
    while q:
        nu, c = q.popleft()
        if count < cnt:
            return
        if nu == m:
            count = min(count, c)
            return 
        for i in range(4):
            if i == 0:
                num1 = nu + 1
                if 0 < num1 <= 1000000 and not visit[num1]:
                    visit[num1] = 1
                    q.append((num1, c + 1))
            elif i == 1:
                num1 = nu - 1
                if 0 < num1 <= 1000000 and not visit[num1]:
                    visit[num1] = 1
                    q.append((num1, c + 1))
            elif i == 2:
                num1 = nu * 2
                if 0 < num1 <= 1000000 and not visit[num1]:
                    visit[num1] = 1
                    q.append((num1, c + 1))
            else:
                num1 = nu - 10
                if 0 < num1 <= 1000000 and not visit[num1]:
                    visit[num1] = 1
                    q.append((num1, c + 1))

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    visit = [0] * 1000001
    count = 10000000000
    BFS(n, 0)
    print('#{} {}'.format(tc, count))