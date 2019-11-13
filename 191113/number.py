# 순열
# 최소값 최대값 차이
import sys
sys.stdin = open('number.txt', 'r')

def perm(k, n):
    global max_num, min_num
    result = numbers[0]
    if k == N - 1:
        a = choose[::]
        if a in choose_list:
            return
        choose_list.append(a)
        idx = 1
        for oper in a:
            if oper == '+':
                result += numbers[idx]
                idx += 1
            elif oper == '-':
                result -= numbers[idx]
                idx += 1
            elif oper == '*':
                result *= numbers[idx]
                idx += 1
            elif oper == '/':
                result /= numbers[idx]
                result = int(result)
                idx += 1
            # print(result, idx)
        if result < min_num:
            min_num = result
        if result > max_num:
            max_num = result
        return
    for i in range(N - 1):
        if not visit[i]:
            visit[i] = 1
            choose.append(operators[i])
            perm(k + 1, n)
            choose.pop()
            visit[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_oper = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    operators = []
    max_num = -(10**8) - 1
    min_num = 10**8 + 1
    for i in range(4):
        if i == 0:
            for j in range(num_oper[i]):
                operators.append('+')
        if i == 1:
            for j in range(num_oper[i]):
                operators.append('-')
        if i == 2:
            for j in range(num_oper[i]):
                operators.append('*')
        if i == 3:
            for j in range(num_oper[i]):
                operators.append('/')
    choose = []
    choose_list = []
    visit = [0] * N
    perm(0, N - 1)
    print('#{} {}'.format(tc, max_num-min_num))