import sys
sys.stdin = open('sample_input1.txt', 'r')

for _ in range(10):
    n = int(input())
    ladder = [list(map(int,input().split())) for i in range(100)]
    
    start_x = start_y = 0
    for p in range(100):
        for q in range(100):
            if ladder[p][q] == 2:
                start_x = p
                start_y = q
    
    x = 99
    while x != 0:
        if ladder[x][start_y - 1] != 1 and ladder[x][start_y + 1] != 1 and ladder[x-1][start_y] == 1:
            x -= 1
        elif ladder[x][start_y - 1] == 1:
            start_y -= 1
        elif ladder[x][start_y + 1] == 1:
            start_y += 1
        


        # for row in range(98, -1, -1):
        #     if ladder[row][start_y] == 1:



