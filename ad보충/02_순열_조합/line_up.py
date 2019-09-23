import sys
from pprint import pprint
sys.stdin = open('line_up.txt' ,'r')

T = int(input())
for tc in range(T):
    arr =  [list(map(int, input().split())) for _ in range(11)]
    visit = [0] * 11
    # pprint(arr)
    sum_list = []
    choose = []
    maxi = 0
    def perm(sum1, row):
        global maxi
        # if sum1 < maxi:
        #     return
        if row == 11 and sum1>=maxi:
            maxi = sum1
            sum_list.append(maxi)
            return
        for i in range(11):
            if not visit[i]:
                if arr[row][i] != 0:
                    visit[i] = 1
                    perm(sum1 + arr[row][i], row + 1)
                    visit[i] = 0
    perm(0, 0)
    print(sum_list)
    # print(maxi)