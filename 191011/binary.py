# 완전이진트리 -> inorder로 값 넣기..-> 마지막노드의 부모노드, 루트값 출력
# 중위순회 이용해서 값 넣기...2i로 왼쪽 노드 찾아가서
# 완전이진트리 만들기.... -> 노드의 개수
import sys
sys.stdin = open('5176.txt')

# 중위순회를 이용하면 오름차순으로 정렬된다!!!
def makeTree(i):
    global index
    if i <= n:  # 노드번호는 노드 개수 보다 작아야한다.
        makeTree(i*2) # 왼쪽서브트리로
        tree[i] = index
        index += 1
        makeTree(i * 2 + 1) # 오른쪽 서브트리로

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    index = 1
    tree = [0 for _ in range(n+1)]
    makeTree(1)
    print('#{} {} {}'.format(tc, tree[1], tree[n//2]))