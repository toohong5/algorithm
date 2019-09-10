import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())
for tc in range(1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    
    # password = []
    # for i in range(N):
    #     for j in range(M):
    #         if arr[i][j] != '0':
    #             password += arr[i][j]
    #     if '0' not in password:
    #         break
    # print(password)