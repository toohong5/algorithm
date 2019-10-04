import sys
sys.stdin = open('weighning_machine.txt', 'r')

def perm(k, n):
    # if sum(left) < sum(right):
    #     return
    if len(left) != 0:
        for a in weights:
            if a not in left:
                right.append(a)
    if sum(left) < sum(right):
        right = []
        perm(k + 1, n)
    if k == n:
        print(*left)
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            left.append(weights[i])
            perm(k + 1, n)
            visit[i] = 0
            left.pop()


# def subset(arr):
#     count = 0
#     for i in range(1 << len(arr)):
#         left = []
#         for j in range(len(arr)):
#             if i & (1 << j):
#                 left.append(arr[j])
#         right = []
#         for a in arr:
#             if a not in left:
#                 right.append(a)
#         if sum(left) >= sum(right):
#             if len(right) != 0:
#                 count += factorial(N)*factorial(N-len(left))//factorial(len(left)) + factorial(N)*factorial(N-len(right))/factorial(len(right))
#             else:
#                 count += factorial(N)*factorial(N-len(left))//factorial(len(left))
            # print(left)
            # print(right)
            # if len(right) != 0:
            #     count += factorial(len(left)) * factorial(len(right))
            # else:
            #     count += factorial(len(left))
            # print(count)
            # count += factorial()
            # print(left)
            # print(right)
            # if len(left) != 1 and len(right) != 1:
            #     count += factorial(len(left)) + factorial(len(right))
            # elif len(left) != 1 and len(right) == 1:
            #     count += factorial(len(left))
            # elif len(right) != 1 and len(left) == 1:
            #     count += factorial(len(left))
    # return count

T = int(input())
for tc in range(1):
    N = int(input())
    weights = list(map(int, input().split()))
    visit = [0] * N
    left = []
    right = []
    perm(0, N)
    # subset(weights)
    # print(subset(weights))