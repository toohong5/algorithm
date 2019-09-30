import sys
sys.stdin = open('score.txt', 'r')

# def perm(k, n):
#     global num_scores
#     if k == N:
#         # print(*choose)
#         num = 0
#         for j in range(len(scores)):
#             num += (choose[j] * scores[j])
#         if num not in score_list:
#             score_list.append(num)
#             num_scores += 1
#         return
#     for i in range(2):
#         choose.append(i)
#         perm(k + 1, n)
#         choose.pop()

# def comb(sum1, s):
#     global num_scores
#     if sum1 not in score_list:
#         score_list.append(sum1)
#         # num_scores += 1
#     for i in range(s, N):
#         comb(sum1 + scores[i], i + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    score_set = {0}

    for i in scores:
        for j in list(score_set):
            score_set.add(i + j)
    print('#{} {}'.format(tc, len(score_set)))





    # for _ in range(N):
    #     choose = []
    #     for i in range(N):
    #         sum1 += scores[i]
    #         if sum1 not in score_list:
    #             score_list.append(sum1)
            
    #         choose.append(scores[i])

    #     # sum2 = 0
    #     if not visit[i]:
    #         visit[i] = 1
    #         if scores[i] not in score_list:
    #             score_list.append(scores[i])
    #             sum1 += scores[i]
    #     sum2 += scores[i]
    #     if sum1 not in score_list:
    #         score_list.append(sum1)
    #     elif sum2 not in score_list:
    #         score_list.append(sum2)


    # comb(0, 0)
    # print(score_list)
    # print('#{} {}'.format(tc, len(score_list)))