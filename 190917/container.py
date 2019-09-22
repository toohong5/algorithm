import sys
sys.stdin = open('container.txt', 'r')

T = int(input())
for tc in range(1):
    N, M = map(int, input().split()) # 화물 수, 트럭 수
    weight = list(map(int, input().split()))
    capacity = list(map(int, input().split()))
    weight.sort(reverse=True)
    capacity.sort()
    result = 0
    for i in range(len(capacity)):
        for j in range(len(weight)):
            if capacity[i] >= weight[j]:
                result += weight[j]
                weight[j] = 200
                break
    print('#{} {}'.format(tc, result))
