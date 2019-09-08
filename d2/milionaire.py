import sys
sys.stdin = open('milionaire.txt', 'r')
sys.setrecursionlimit(10**9)
def my_func(start, end, profit):
    # global profit
    global max_price
    if start == len(arr):
        return 1
    for i in range(start, end):
        if max_price < arr[i]:
            max_price = arr[i]
    end = arr.index(max_price)
    for j in range(start, end):
        profit += (max_price - arr[j])
    start = end + 1
    end = len(arr)
    max_price = 0
    my_func(start, end, profit)
        
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    start = 0
    max_price = 0
    profit = 0

    for i in range(len(arr)-1, -1, -1):
        if max_price < arr[i]:
            max_price = arr[i]
        else:
            profit += (max_price - arr[i])
    print('#{} {}'.format(tc, profit))
    
    # buy = []
    # end = len(arr)
    # while start != len(arr):
    #     for i in range(start, end):
    #         if max_price < arr[i]:
    #             max_price = arr[i]
    #     end = arr.index(max_price)
    #     for j in range(start, end):
    #         profit += (max_price - arr[j])
    #     start = end + 1
    #     end = len(arr)
    #     max_price = 0

    # my_func(start, len(arr), max_price)