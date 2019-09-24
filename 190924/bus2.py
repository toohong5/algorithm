import sys
sys.stdin = open('bus2.txt', 'r')
# 
def charge(b, count, i):
    global min_count
    if i == N - 1:
        min_count = min(count, min_count)
        return
    if b > 0: # 교체 하지 않고 이동
        charge(b - 1, count, i + 1)
    if b >= 0: # 교체하고 이동
        charge(battery[i] - 1, count + 1, i + 1)

T = int(input())
for tc in range(1, T + 1):
    N, *battery = map(int, input().split())
    min_count = 50000000
    charge(battery[0], 0, 0)
    print('#{} {}'.format(tc, min_count))

# ---------------------------------------------------------

# 현재 정류장 번호, 잔량, 충전 횟수
# DP로 풀기...?