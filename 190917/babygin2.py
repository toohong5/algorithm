import sys
sys.stdin = open('babygin.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    player1 = arr[0:12:2]
    player2 = arr[1:13:2]
    result1 = result2 = 0
    s1, s2 = player1[:3], player2[:3]

    for i in range(3, len(player1)+1):
        for j in range(len(s1)):
            if s1.count(s1[j]) >= 3:
                result1 = 1
            elif (s1[j]-1 in s1 and s1[j] + 1 in s1):
                result1 = 1
            if s2.count(s2[j]) >= 3:
                result2 = 2
            elif (s2[j]-1 in s2 and s2[j] + 1 in s2):
                result2 = 2
            if result1 != 0 or result2 != 0:
                break
        if result1 !=0 or result2 != 0:
            break
        else:
            if i != len(player1):
                s1.append(player1[i])
                s2.append(player2[i])
            else:
                break
    # print(s1)
    # print(s2)
    if result1 == 0 and result2 == 0:
        print('#{} 0'.format(tc))
    if result1 == 1 and result2 == 0:
        print('#{} {}'.format(tc, result1))
    if result2 == 2 and result1 == 0:
        print('#{} {}'.format(tc, result2)) 
    if result1 == 1 and result2 == 2:
        print('#{} 0'.format(tc))