import sys
sys.stdin = open('im_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room = list(map(int,input().split()))
    led = [0] * N
    count = 0
    # while led != room:
    for i in range(N):
        if room[i] == 1:
            if i+1 == 1:
                for j in range(0, N, i+1):
                    if led[j] == 0:
                        led[j] = 1
                    else:
                        led[j] = 0
            # elif i+1 == 2:
            #     for j in range(N, 2):
            #         if led[j] == 0:
            #             led[j] = 1
            #         else:
            #             led[j] = 0
            # count += 1
            
            # for j in range(N):
            #     if (j + 1) % (i + 1) == 0:
            #         if led[j] == 0:
            #             led[j] = 1
            #             if room == led:
            #                 break
            #         else:
            #             led[j] = 0
            #             if room == led:
            #                 break
    
    print(led) 
    print('#{} {}'.format(tc, count))