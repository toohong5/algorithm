import sys
sys.stdin = open('babygin.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    player1 = arr[0:12:2]
    player2 = arr[1:13:2]
    # print(player1)
    # print(player2)
    S1 = player1[:3]
    S2 = player2[:3]
    # print(S1)
    # print(S2)
    result = 0
    result1 = 0
    result2 = 0
    for k in range(len(S1)):
        if S1.count(S1[k]) == 3 or (S1[k] - 1 in S1 and S1[k] + 1 in S1):
            result1 = 1
        if S2.count(S2[k]) == 3 or (S2[k] - 1 in S2 and S2[k] + 1 in S2):
            result2 = 2
        if result1 != 0 or result2 != 0:
            break
    if result1 == 0 and result2 == 0:
        for j in range(3, 6):
            S1.append(player1[j])
            S2.append(player2[j])
            for k in range(len(S1)):
                if S1.count(S1[k]) == 3 or (S1[k] - 1 in S1 and S1[k] + 1 in S1):
                    result1 = 1
                if S2.count(S2[k]) == 3 or (S2[k] - 1 in S2 and S2[k] + 1 in S2):
                    result2 = 2
                if result1 != 0 or result2 != 0:
                    break
            if result1 != 0 or result2 != 0:
                break

    if result1 != 0 and result2 != 0:
        result = 0
    if result1 == 1 and result2 == 0:
        result = 1
    if result2 == 2 and result1 == 0:
        result = 2
    if result1 == 2 and result1 == 1:
        result = 0
    # print(S1)
    # print(S2)
    print('#{} {}'.format(tc, result))
    # for i in range(6):
    #     if i == 3:
    #         for k in range(len(S1)):
    #             if S1.count(S1[k]) == 3 or (S1[k] - 1 in S1 and S1[k] + 1 in S1):
    #                 result1 = 1
    #             if S2.count(S2[k]) == 3 or (S2[k] - 1 in S2 and S2[k] + 1 in S2):
    #                 result2 = 2
    #             if result1 != 0 or result2 != 0:
    #                 break
    #         if result1 != 0 or result2 != 0:
    #                 break
    #         # S1.sort()
    #         # S2.sort()
    #         # if S1.count(S1[0]) == 3 or (S1[1] - 1 in S1 and S1[1] + 1 in S1):
    #         #     result1 = 1
    #         # if S2.count(S2[0]) == 3 or (S2[1] - 1 in S2 and S2[1] + 1 in S2):
    #         #     result2 = 2
    #         # if result1 != 0 and result2 != 0:
    #         #     break
    #         else:
    #             for j in range(3, 6):
    #                 S1.append(player1[j])
    #                 S2.append(player2[j])
    #                 for k in range(len(S1)):
    #                     if S1.count(S1[k]) == 3 or (S1[k] - 1 in S1 and S1[k] + 1 in S1):
    #                         result1 = 1
    #                     if S2.count(S2[k]) == 3 or (S2[k] - 1 in S2 and S2[k] + 1 in S2):
    #                         result2 = 2
    #                     if result1 != 0 or result2 != 0:
    #                         break
    #                 if result1 != 0 or result2 != 0:
    #                     break
    #             if result1 != 0 or result2 != 0:
    #                 break                   
    #     else:
    #         S1.append(player1[i])
    #         S2.append(player2[i])
