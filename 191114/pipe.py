# 상하 좌우로 나갈 수 있는 형태의 터널종류 => out
# 하상 우좌로 들어올 수 있는 터널의 종류 => in
# 출발 가능한지 체크 -> 원 위치의 파이프 종류 파악 -> 좌표 이동 후 아래에서 이동한 자리로 연결되어 있는지 파악

# 나갈 수 있는지 먼저 파악(out에 들어있는지..) -> 좌표 이동 후 그 파이프가 in에 들어있는지 파악..
import sys
sys.stdin = open('pipe.txt', 'r')
from collections import deque
def bfs(x, y, nums):
    q = deque()
    q.append((x, y, nums))
    visit[x][y] = 1
    while q:
        i, j, times = q.popleft()
        if times == l:
            return
        for k in range(4):
            if arr[i][j] in OUT[k]:
                x1 = i + dx[k]
                y1 = j + dy[k]
                if 0 <= x1 < n and 0 <= y1 < m:
                    if arr[x1][y1] not in IN[k]: continue
                    if not visit[x1][y1]:
                        visit[x1][y1] = 1
                        q.append((x1, y1, times+1))
                          
IN = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]
OUT = [[1, 2, 4, 7], [1, 2, 5, 6], [1, 3, 6, 7], [1, 3, 4, 5]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    n, m, x, y, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    count = 0
    bfs(x, y, 1)
    for k in range(len(visit)):
        count += visit[k].count(1)
    print('#{} {}'.format(tc, count))