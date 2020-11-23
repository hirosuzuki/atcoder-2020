from collections import Counter

N = input()

def resolve(N):
    cs = [int(c) for c in N]
    l = len(cs)
    m = sum(cs) % 3
    cs3 = [0, 0, 0]
    for c in cs:
        cs3[c % 3] += 1
    # print(m, cs3)
    if m == 0:
        return 0
    if m == 1:
        if cs3[1] >= 1 and l > 1:
            return 1
        if cs3[2] >= 2 and l > 2:
            return 2
        return -1
    if m == 2:
        if cs3[2] >= 1 and l > 1:
            return 1
        if cs3[1] >= 2 and l > 2:
            return 2
        return -1

result = resolve(N)
print(result)
