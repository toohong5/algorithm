import sys
sys.stdin = open('input3.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = 5
    arr = [list(input()) for _ in range(N)]
    max_len = 0
    col_arr = []
    for i in range(len(arr)):
        if max_len < len(arr[i]):
            max_len = len(arr[i])
    
    for row in range(len(arr)):
        if len(arr[row]) != max_len:
            while len(arr[row]) != max_len:
                arr[row].append('')

    for j in range(len(arr[0])):
        w = ''
        for i in range(len(arr)):
            w += arr[i][j]
        col_arr.append(w)
    
    print('#{}'.format(tc), end=' ')
    for i in col_arr:
        print(i, end='')
    print()
    
    


    
