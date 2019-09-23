import sys
sys.stdin = open('input.txt', 'r')
# 순열로 푼다...
# 순열, 완전탐색, 부분집합....잘하기...
def perm(per, row): # 1~16(0~15)까지 번호 나열
    global maximum  # 지금까지 발견한 가장 좋은 해
    if per * 100 <= maximum:    #  가지치기( 최소값의 경우 가지치기 쉬움.. 커지면 버리면 됨...최대값이면.. 갈 수록 커질 수 도 있으니...끊으면 안된다..이경우 1보다 작은 값을 곱해서 작아지므로 상관 없었음...)
        return
    if row == N and (per * 100 > maximum):
        maximum = per * 100
        return 
    else:
        for i in range(N):
            if visit[i] == 0:
                visit[i] = 1
                perm(per * arr[row][i], row + 1)
                visit[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visit = [0] * 17
    arr = [list(map(int, input().split())) for _ in range(N)]
    maximum = 0
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] / 100

    perm(1.0, 0)
    print('#%d %.6f'%(tc, maximum))

    #-----------------------------
    # 임의의 최적해를 탐욕으로 먼저 구해놓는다...
    # 이 해를 가지치기에 이용...

    ans, cnt = 100.0, 0
    col = [0]*N
    for i in range(N):
        MAX, idx = 0, 0
        for j in range(N):
            if col[j] == 0 and MAX < G[i][j]:
