import sys
sys.stdin = open('sample_input5.txt', 'r')

for tc in range(10):
    n = int(input())
    arr = [input() for i in range(100)]
    N = len(arr)
    M = 1
    count = 0
    length_m = []
    #-------------------------
    # 세로행렬
    col_list = []
    for c in range(N):
        w = ''
        for r in range(N):
            w += arr[r][c]
        col_list.append(w)
    # print(col_list)
    for row in arr:
        while M <= N:
            for start in range(N-M+1):
                end = start + M
                if row[start:end] == row[start:end][::-1]:
                    if M not in length_m:
                        length_m.append(M)
            M += 1
        M  = 1
        
    for col in col_list:
        while M <= N:
            for start in range(N-M+1):
                end = start + M
                if col[start:end] == col[start:end][::-1]:
                    if M not in length_m:
                        length_m.append(M)
            M += 1
        M = 1
        
    print('#{} {}'.format(tc+1, max(length_m)))
                
    # for row in range(N):
    #     for start in range(N - M + 1):
    #         end = start + M - 1
    #         for i in range(M // 2):
    #             if arr[row][start + i] != arr[row][end - i]:
    #                 break
    #         else:
    #             if M not in length_m:
    #                 length_m.append(M)
    #             M += 1
    
    # print(length_m)
    