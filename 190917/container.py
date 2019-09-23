import sys
sys.stdin = open('container.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # 화물 수, 트럭 수
    weight = list(map(int, input().split()))
    capacity = list(map(int, input().split()))
    weight.sort(reverse=True)
    capacity.sort(reverse=True)
    result = 0
    visit = [0] * N
    for i in range(len(capacity)):
        for j in range(len(weight)):
            if not visit[j]:
                if capacity[i] >= weight[j]:
                    result += weight[j]
                    visit[j] = 1
                    # weight[j] = 200
                    # break
    print('#{} {}'.format(tc, result))
