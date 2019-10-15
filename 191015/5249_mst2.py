import sys
sys.stdin = open('5249.txt', 'r')

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    Edge = []
    for _ in range(E):
        Edge.append(tuple(map(int, input().split())))
    
    Edge.sort(key = lambda x: x[2])
    p = [x for x in range(V + 1)]
    # 부모찾기(루트)
    def find_set(x):
        if x != p[x]:
            p[x] = find_set(p[x])
        return p[x]

    MST = []
    cnt = V
    idx = 0
    print(Edge)
    while cnt > 0:
        u, v, w = Edge[idx]
        a = find_set(u)
        b = find_set(v)
        if a != b:  # 서로 연결 안되었을 때 => 연결시켜주기
            p[b] = a
            MST.append((u, v, w))
            cnt -= 1
            idx += 1
        else:   # 연결 되어있으니 패스!
            idx += 1

    sum_edge = 0
    for edge in MST:
        sum_edge += edge[2]
    print('#{} {}'.format(tc, sum_edge))