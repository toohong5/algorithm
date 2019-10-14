import sys
sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())
Edge = []   # 간선들의 리스트를 튜플로 저장
for _ in range(E):
    Edge.append(tuple(map(int, input().split())))

# 가중치순으로 오름차순 정렬
Edge.sort(key = lambda x: x[2])
p = [x for x in range(V)]
def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]
# V - 1 개의 간선을 선택
MST = [] # 간선을 저장
cur = 0 # 하나씩 읽어오기 위한 인덱스
while len(MST) < V - 1:
    u, v, w = Edge[cur]
    a = find_set(u); b = find_set(v)
    if a != b:
        p[b] = a # 다를 때 합침
        MST.append((u, v, w))
    cur += 1

for edge in Edge:
    print(edge, end=' ')