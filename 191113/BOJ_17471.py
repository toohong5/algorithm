import sys
sys.stdin = open('17471.txt', 'r')
from collections import deque

def DFS(s, group):
    visit[s] = 1
    ret = False
    for w in G[v]:
        if w in group and not visit[w]:
            ret += DFS(w, group)
    return ret

def subset(k):
    global least
    result1 = result2 = False
    if k == N + 1:
        # print(t1, t2)
        town1 = t1[::]
        town2 = t2[::]
        result1 = DFS(town1[0], t1)
        result2 = DFS(town2[0], t2)
        print(result1, result2)
        # num1 = num2 = 0
        # if result1 == True and result2 == True:
        #     for p in t1:
        #         num1 += people[p]
        #     for q in t2:
        #         num2 += people[q]
        #     if least > abs(num1 - num2):
        #         least = abs(num1 - num2)
    else:
        t1.append(k)
        subset(k + 1)
        t1.pop()

        t2.append(k)
        subset(k + 1)
        t2.pop()

N = int(input())
people = list(map(int, input().split()))
G = [[] for _ in range(N + 1)]
visit = [0] * (N + 1)
least = 5000
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(1, len(arr)):
        G[i+1].append(arr[j])
        # G[arr[j]].append(i + 1)
# print(G)
t1, t2 = [], []
subset(1)
if least == 5000:
    least = -1
print(least)