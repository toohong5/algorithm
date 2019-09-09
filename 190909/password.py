import sys
sys.stdin = open('input1.txt', 'r')
import pprint
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    password = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    check=[]

    x = y = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                x, y = i, j
        if arr[x][y] == 1:
            break
    w = ''
    for i in range(y-55, y + 1):
        w += str(arr[x][i])

    for i in range(0, len(w), 7):
        w2 = ''
        for j in range(i, i+7):
            w2 += w[j]
        check.append(w2)

    for c in range(len(check)):
        for p in password:
            if p == check[c]:
                check[c] = password.index(p)
    odd_sum = 0
    even_sum = 0
    for i in range(0, len(check), 2):
        odd_sum += check[i]
    for i in range(1, len(check), 2):
        even_sum += check[i]
    code = 0
    code = odd_sum * 3 + even_sum 
    result = 0
    if code % 10 == 0:
        result = sum(check)
    else:
        result = 0
    print('#{} {}'.format(tc, result))