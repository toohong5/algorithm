import sys
sys.stdin = open('input2_5.txt', 'r')

N = int(input())

for i in range(1, N + 1):
    n = int(input())
    length_list = list(map(int, input().split()))
    l_list = []
    # 수나사 굵기, 암나사 굵기를 리스트로 묶음
    while len(l_list) != n:
        l_list.append([length_list[0], length_list[1]])
        length_list.remove(length_list[0])
        length_list.remove(length_list[0])

    # 기준 : [1]
    N = len(l_list)
    M = len(l_list[0])
    min_y = 0
    for p in range(N):
        for q in range(M):
            min_y = min(l_list[p][1])
    print(min_y)
    result = []

