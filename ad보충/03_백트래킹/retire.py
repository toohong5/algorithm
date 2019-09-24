import sys
sys.stdin = open('retire.txt', 'r')

def counseling(pay, row):
    global max_sum
    if row == N - 1:
        if arr[row][0] == 1:
            pay += arr[row][1]
        max_sum = max(pay, max_sum)
        return
    if row == N:
        max_sum = max(pay, max_sum)
        return
    if row > N - 1:
        return
    counseling(pay + arr[row][1], row + arr[row][0])
    counseling(pay, row + 1)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# visit = [0] * N
max_sum = 0
counseling(0, 0)
print(max_sum)
