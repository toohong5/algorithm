import sys
sys.stdin = open('memory.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input()))
    memory = [0] * len(arr)
    count = 0

    i = 0
    while arr != memory:
        if arr[i] != memory[i]:
            for j in range(i, len(memory)):
                memory[j] = arr[i]
            count += 1
        i += 1
    print('#{} {}'.format(tc, count))

