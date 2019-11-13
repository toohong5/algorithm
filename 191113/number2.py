import sys
sys.stdin = open('number.txt', 'r')

def cal(idx):
    global result, max_num, min_num
    if idx == N:
        if result > max_num:
            max_num = result
        if result < min_num:
            min_num = result
        return
    for i in range(4):
        if num_oper[i] > 0:
            num_oper[i] -= 1
            temp = result
            if i == 0:
                result += numbers[idx]
            elif i == 1:
                result -= numbers[idx]
            elif i == 2:
                result *= numbers[idx]
            elif i == 3:
                if numbers[idx] != 0:
                    result /= numbers[idx]
                    result = int(result)
                else:
                    num_oper[i] += 1
                    continue
            cal(idx+1)
            result = temp
            num_oper[i] += 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_oper = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    max_num = -(10**8) - 1
    min_num = 10**8 + 1
    result = numbers[0]
    cal(1)
    print('#{} {}'.format(tc, max_num - min_num))