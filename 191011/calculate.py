import sys
sys.stdin = open('calculate.txt', 'r')

def inorder(n):
    if n != 0:
        inorder(child[n][0])
        
        inorder(child[n][1])

for tc in range(1):
    n = int(input())
    cal = [''] * (n + 1)
    child = [[0] * 2 for _ in range(n + 1)]
    for _ in range(n):
        arr = list(input().split())
        if len(arr) == 3:
            cal[int(arr[0])] = arr[1]
            child[int(arr[0])][0] = int(arr[2])
        elif len(arr) == 4:
            cal[int(arr[0])] = arr[1]
            child[int(arr[0])][0] = int(arr[2])
            child[int(arr[0])][1] = int(arr[3])
        else:
            child[int(arr[0])][0] = int(arr[1])
    print(cal)
    print(child)