import sys
sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())
G = [[] for _ in range(V)] # 0 ~ V-1

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w)) # 인접 정점과 간선의 가중치 함께 저장
    G[v].append((u, w))

key = [0xfffff] * V
pi = [-1] * V # -1 => NULL
visit = [False]  * V # 트리에 포함된 정점과 아닌 정점들 구분하기 위해서 사용
key[0] = 0  # 시작점 0의 key 값 초기화
cnt = V
while cnt: # 정점의 개수 만큼 반복
    # key 값이 최소인 정점을 찾는다 
    u, MIN = 0, 0xfffff
    for i in range(V):
        if not visit[i] and MIN > key[i]: # 방문하지 않은애 찾아서 키값과 비교해 가장 작은 값 저장
            u, MIN = i, key[i]
    visit[u] = True
    # u의 인접정점을 찾아서 key, pi를 변경
    for v, w in G[u]: # v, w : 정점, 가중치
        if not visit[v] and w < key[v]:
            key[v] = w
            pi[v] = u
    cnt -= 1
print(key)
# 우선순위 큐?