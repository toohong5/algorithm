import sys
sys.stdin = open('max_prize.txt', 'r')

def change(count, num, s):
    global max_num
    if count == N:
        if num > max_num:
            max_num = num
        return
    for i in range(s, len(arr)):    # 시작범위 바꾸기..
        for j in range(i + 1, len(arr)):
            if arr[i] <= arr[j]:    # 바꿀애가 더 작으면 안바꿈...
                arr[i], arr[j] = arr[j], arr[i]
                num = int(''.join(arr))
                change(count + 1, num, i)
                arr[i], arr[j] = arr[j], arr[i]

T = int(input())
for tc in range(1, T + 1):
    arr, N = map(int, input().split())
    arr = list(str(arr))
    max_num = 0
    change(0, 0, 0)
    print('#{} {}'.format(tc, max_num))
    # *arr, B, N = map(str,input())
    # if B != ' ': N = B + N
    # N = int(N)
    # print(arr)
    # count = 0
    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    #         if i != j:
    #             arr[i], arr[j] = arr[j], arr[i]
    #             count += 1
    #             num = int(''.join(arr))
    #             if count == N:
    #                 if num > max_num:
    #                     max_num = num
    #                     arr[i], arr[j] = arr[j], arr[i]
    #                     count -= 1
    #                 else:
    #                     arr[i], arr[j] = arr[j], arr[i]
    #                     count -= 1