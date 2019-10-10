import sys
sys.stdin = open('input.txt', 'r')

def preorder(n): # 전위순회
    if n != 0:
        print(n, end=" ")
        preorder(child[n][0]) # 왼쪽
        preorder(child[n][1]) # 오른쪽
        
def inorder(n): # 중위순회
    if n != 0:
        inorder(child[n][0]) # 왼쪽
        print(n, end=" ")
        inorder(child[n][1]) # 오른쪽
        
def postorder(n): # 후위순회
    if n != 0:
        postorder(child[n][0]) # 왼쪽
        postorder(child[n][1]) # 오른쪽
        print(n, end=" ")

N = int(input())
arr = list(map(int, input().split()))
child = [[0] * 2 for i in range(N+1)]

for k in range(0, len(arr), 2):
    if child[arr[k]][0] == 0: # 왼쪽이 빈 경우
        child[arr[k]][0] = arr[k+1]
    else:
        child[arr[k]][1] = arr[k+1]

# for i in range(N-1):
#     if child[arr[i*2]][0] == 0:   # 부모노드 i*2에 자식이 없는 경우
#         child[arr[i*2]][0] = arr[i*2+1]
#     else:
#         child[arr[i*2]][1] = arr[i*2+1]

print(arr)
print()
print(child)
print()
preorder(1)
print()
inorder(1)
print()
postorder(1)
print()