import sys
sys.stdin = open('5176.txt')

def inorder(i):
    global index
    if i <= n:
        inorder(2*i)
        tree[i] = index
        index += 1
        inorder(2*i+1)

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    tree = [0] * (n + 1)
    index = 1
    inorder(1)
    print('#{} {} {}'.format(tc, tree[1], tree[n//2]))