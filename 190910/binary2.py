import sys
sys.stdin = open('input4.txt', 'r')

def BIN(N):
    global result
    if N * 2 == 1.000:
        result += str(int(N * 2))
        return 1
    i, f = int(N * 2), float(N * 2) - int(N * 2)
    result += str(i)
    N = f
    BIN(N)

T = int(input())

for tc in range(1, T + 1):
    result = ''
    N = float(input())
    BIN(N)
    if len(result) > 12:
        print('#{} overflow'.format(tc))
    else:
        print('#{} {}'.format(tc, result))