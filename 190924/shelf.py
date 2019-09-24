import sys
sys.stdin = open('shelf.txt', 'r')

def perm(s, e, sum):
    global B
    if sum >= B:
        result.append(sum)
    if s == e:
        return
    perm(s + 1, e, sum + heights[s])
    perm(s + 1, e, sum)

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    result = []
    perm(0, N, 0)
    # for i in range(1 << len(heights)):
    #     a = []
    #     for j in range(len(heights)):
    #         if i & (1 << j):
    #             a.append(heights[j])
    #         if sum(a) >= B:
    #             result.append(sum(a) - B)
    print('#{} {}'.format(tc, min(result)-B))