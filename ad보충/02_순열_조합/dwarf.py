import sys
sys.stdin = open('dwarf.txt', 'r')

height = [int(input()) for _ in range(9)]

choose = []
def comb(k, s):
    if k == 7:
        if sum(choose) == 100:
            choose.sort()
            for i in range(len(choose)):
                print(choose[i])
        return
    for i in range(s, len(height)):
        choose.append(height[i])
        comb(k + 1, i + 1)
        choose.pop()
comb(0, 0)