import sys
sys.stdin = open('input4.txt', 'r')

from itertools import permutations, combinations
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # numbers = list(map(int, input().split()))
    mul = []
    mono = []

    for num in combinations(list(map(int, input().split())), 2):
        mul.append(str(num[0] * num[1]))
    # for i in range(len(numbers)):
    #     for j in range(i + 1, len(numbers)):
    #         mul.append(str(numbers[i] * numbers[j]))
    result = 0
    for num in mul:
        if len(num) > 1:
            s = num[0]
            for i in range(1, len(num)):
                if s <= num[i]:
                    s = num[i]
                    result = 1
                else:
                    result = 0
                    break
            if result == 1:
                mono.append(int(num))
    if len(mono) == 0:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc, max(mono)))