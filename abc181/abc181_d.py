S = input()

def solve(S: str) -> bool:
    if len(S) == 1:
        return int(S) % 8 == 0
    if len(S) == 2:
        return int(S) % 8 == 0 or int(S[::-1]) % 8 == 0
    cs = [0] * 10
    for c in S:
        cs[int(c)] += 1
    #print(cs)
    def ycs(cs):
        for i in range(1, 10):
            if cs[i]:
                yield i
    for n1 in ycs(cs):
        if n1 % 2 == 1:
            continue
        cs1 = cs[:]
        cs1[n1] -= 1
        for n2 in ycs(cs1):
            cs2 = cs1[:]
            cs2[n2] -= 1
            for n3 in ycs(cs2):
                nn = n1 + n2 * 10 + n3 * 100
                if nn % 8 == 0:
                    return True
    return False

result = ["No", "Yes"][solve(S)]

print(result)

