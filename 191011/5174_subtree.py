import sys
sys.stdin = open('5174.txt', 'r')
# preorder응용
def preorder(n):
    global count
    if n != 0:
        count += 1
        preorder(child[n][0])
        preorder(child[n][1])

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    child = [[0] * 2 for _ in range(E + 2)]
    count = 0
    for i in range(0, len(arr), 2):
        if child[arr[i]][0] == 0:
            child[arr[i]][0] = arr[i + 1]
        else:
            child[arr[i]][1] = arr[i + 1]
    preorder(N)
    print('#{} {}'.format(tc, count))