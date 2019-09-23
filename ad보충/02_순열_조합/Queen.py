N = 8 
visit = [0] * N
cnt = 0
cols = [0] * N # 퀸의 열 값을 저장
def posstible(k, c):    # k번 퀸의 열 1가 답이 되는 선택인지 조사
    for i in range(k): # 0 ~ k-1번 퀸과 대각 있는지 조사
        if k - i == abs(c - cols[i]):
            return False
    return True
def nQueen(k):
    if k == N:
        global cnt
        cnt += 1
    else:
        for i in range(N):
            if visit[i]: continue
            visit[i] = 1
            cols[k] = i # k번 퀸의 열값을 i로 결정
            nQueen(k + 1)
            visit[i] = 0
    
nQueen(0)
print(cnt)