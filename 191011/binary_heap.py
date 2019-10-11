# 모든 노드들이 자식보다 작거나 커야함..
# 완전이진트리여야 한다.
# 새로운 노드는 가장 마지막에 추가되어야한다. 
import sys
sys.stdin = open('5177.txt', 'r')

def preorder(i):
    global index
    if i > N:
        return
    if index == 0:
        tree[i] = arr[index]
        index += 1
    elif index >= 1:
        if tree[i//2] > arr[index]:
            tree[i] = tree[i//2]
            tree[i//2] = arr[index]
            index += 1
        else:
            tree[i] = arr[index]
            index += 1
    di = [2*i, 2*i+1]
    for j in range(2):
        preorder(di[j])
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N + 1)
    child = [[0] * 2 for _ in range(N + 1)]
    
    index = 0
    preorder(1)
    print(tree)