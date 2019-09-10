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


    # ------------------------------------------------

C = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9
    }

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]

    def find():
        pwd = [0] * 8
        for i in range(N):
            j = M - 1
            while j >= 0:
                if arr[i][j] == '1':
                    for k in range(7, -1, -1):
                        c1 = c2 = c3 = c4 = 0
                        while arr[i][j] == '1':
                            c4, j = c4 + 1, j - 1
                        while arr[i][j] == '0':
                            c3, j = c3 + 1, j - 1
                        while arr[i][j] == '1':
                            c2, j = c2 + 1, j - 1

                        c1 = 7 - (c2 + c3 + c4)
                        pwd[k] = C[(c1, c2, c3, c4)]
                        j -= c1
                    a = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                    b = pwd[1] + pwd[3] + pwd[5] + pwd[7]
                    if (a * 3 + b) % 10 == 0:
                        return a + b
                    else: return 0
                j -= 1
        return 0

    print('#{} {}'.format(tc, find()))
