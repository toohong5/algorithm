import sys
sys.stdin = open('input1.txt', 'r')

def ter(a):
    s = ''
    while a > 0:
        a, r = divmod(a, 3)
        if (r>9):
            r = chr(ord('a') + r - 10)
        s = str(r) + s
    return s

T = int(input())
for tc in range(1, T + 1):
    b = input()
    t = input()
    binary = list(b)
    ternary = list(t)
 
    binary_change = []
    ternary_change = []
    for i in range(len(binary)):
        w = ''
        if binary[i] == '0':
            binary[i] = 1
        elif binary[i] == '1':
            binary[i] = 0
        for j in range(0, len(binary)):
            w += str(binary[j])
        binary_change.append(int(w, 2))
        binary = list(b)

    for bi in binary_change:
        ternary_change.append(ter(bi))
    p = 0
    for te in ternary_change:
        if len(te) == len(t):
            count = 0
            for i in range(len(t)):
                if te[i] != t[i]:
                    count += 1
            if count == 1:
                p = ternary_change.pop(ternary_change.index(te))
    if int(str(p),3) in binary_change:
        print(int(str(p),3))