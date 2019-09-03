import sys
sys.stdin = open('sample_input5.txt', 'r')
from collections import deque

def BFS(start):
    visit = [0] * 101
    q = deque()
    q.append(start)
    visit[start] = 1

    end = []

    while q:
        v = q.popleft()
        for w in G[v]:
            if not visit[w]:
                visit[w] = 1
                if len(G[w]) == 0:
                    q.append(w)
                    end.append(w)
                else:
                    q.append(w)
    return end

for tc in range(1, 11):
    length, start = map(int, input().split())
    G = [[] for _ in range(101)]
    
    arr = list(map(int, input().split()))
    for _ in range(length//2):
        u = arr.pop(0)
        v = arr.pop(0)
        G[u].append(v)
    
    print('#{} {}'.format(tc, max(BFS(start))))

