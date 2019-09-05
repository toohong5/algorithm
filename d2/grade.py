import sys
sys.stdin = open('grade.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(N)]
    grades = []
    char_grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    num = N // 10
    for score in scores:
        grades.append(score[0]*0.35 + score[1]*0.45 + score[2]*0.2)

    grade = sorted(grades, reverse=True)
    final = sorted(grades, reverse=True)
    for c in char_grades:
        for _ in range(num):
            final.pop(0)
            final.append(c)

    for k in range(N):
        if k+1 == K:
            print('#{} {}'.format(tc, final[grade.index(grades[k])]))

