import sys
sys.stdin = open('cook.txt', 'r')

def subset(k):
    global min_dish
    if k == n + 1:
        dish1 = dish2 = 0
        if len(a) == n//2:
            for i in range(len(a)):
                for j in range(i + 1, len(a)):
                    if i != j:
                        dish1 += cook[a[i]-1][a[j]-1]+cook[a[j]-1][a[i]-1]
                        dish2 += cook[b[i]-1][b[j]-1]+cook[b[j]-1][b[i]-1]
            if abs(dish1 - dish2) < min_dish:
                min_dish = abs(dish1 - dish2)
    else:
        a.append(k)
        subset(k + 1)
        a.pop()

        b.append(k)
        subset(k + 1)
        b.pop()

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    cook = [list(map(int, input().split())) for _ in range(n)]
    a, b = [], []
    min_dish = 500000
    subset(1)
    print('#{} {}'.format(tc, min_dish))