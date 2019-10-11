import sys
sys.stdin = open('inorder.txt', 'r')

def inorder(n):
    if n != 0:
        inorder(child[n][0])
        print(words[n], end='')
        inorder(child[n][1])

for tc in range(1, 11):
    N = int(input())
    words = [''] * (N + 1)
    child = [[0] * 2 for _ in range(N + 1)]
    for _ in range(N):
        arr = list(input().split())
        if len(arr) == 3:
            words[int(arr[0])] = arr[1]
            child[int(arr[0])][0] = int(arr[2])
        elif len(arr) == 4:
            words[int(arr[0])] = arr[1]
            child[int(arr[0])][0] = int(arr[2])
            child[int(arr[0])][1] = int(arr[3])
        else:
            words[int(arr[0])] = arr[1]
    print('#{}'.format(tc), end=' ')
    inorder(1)
    print()




            if tree[i//2] > arr[index]:
                if tree[i] == 0:
                    tree[i] = tree[i//2]
                    tree[i//2] = arr[index]
                    i += 1
                    index += 1
                else:
                    tree[i + 1] = arr[index]
                    i *= 2
                    index += 1
            else:
                if tree[i] == 0:
                    tree[i] = arr[index]
                    i += 1
                    index += 1
                else:
                    tree[i + 1] = arr[index]
                    i *= 2
                    index += 1

j = i
            while j != 0:
                if tree[j//2] > arr[index]:
                    if tree[j] == 0:
                        tree[j] = tree[j//2]
                        tree[j//2] = arr[index]
                        i += 1
                        index += 1
                    else:
                        tree[j + 1] = arr[index]
                        i *= 2
                        index += 1
                else:
                    if tree[j] == 0:
                        tree[j] = arr[index]
                        i += 1
                        index += 1
                    else:
                        tree[j + 1] = arr[index]
                        i *= 2
                        index += 1
                j = j // 2