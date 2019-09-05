import sys
sys.stdin = open('369.txt', 'r')

N = int(input())

arr = [str(i) for i in range(1, N + 1)]

for i in arr:
    count = 0
    if ('3' in i) or ('6' in i) or ('9' in i):
        count += i.count('3')
        count += i.count('6')
        count += i.count('9')
        print('-'*count, end = ' ')
    else:
        print(int(i), end = ' ')
