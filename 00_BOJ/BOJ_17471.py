import sys
sys.stdin = open('17471.txt', 'r')
from collections import deque

def DFS(s, group, visit):
    visit[s] = 1
    ret = 1
    for w in G[s]:
        if w in group and not visit[w]:
            ret += DFS(w, group, visit)
    return ret

def subset(k):
    global least
    if k == N + 1:
        if len(t1) != 0 and len(t2) != 0:
            r1 = r2 = 0
            visit = [0] * (N + 1)
            r1 = DFS(t1[0], t1, visit)
            visit = [0] * (N + 1)
            r2 = DFS(t2[0], t2, visit)
            num1 = num2 = 0
            if r1 + r2 == N:
                for p in t1:
                    num1 += people[p-1]
                for q in t2:
                    num2 += people[q-1]
                if least > abs(num1 - num2):
                    least = abs(num1 - num2)
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

least = 5000
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(1, len(arr)):
        G[i+1].append(arr[j])
t1, t2 = [], []
subset(1)
if least == 5000:
    least = -1
print(least)