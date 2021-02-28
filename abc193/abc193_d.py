from typing import List

N = int(input())
S = input()
T = input()

def solve(N: int, S: str, T: str):
    def calc_score(xs: List[int]) -> int:
        cs = [0] * 10
        for x in xs:
            cs[x] += 1
        return sum(i * 10**(cs[i]) for i in range(1, 10))

    ss = [int(S[i]) for i in range(4)]
    ts = [int(T[i]) for i in range(4)]
    ls = [N] * 10
    for x in ss + ts:
        ls[x] -= 1
    ctotal = N * 9 - 8

    #print(ss, ts, ls, ctotal)
    #print(calc_score([1,1,4,4,9]))

    result = 0
    for i in range(1, 10):
        if ls[i] < 1:
            continue
        s1 = calc_score(ss + [i])
        r = ls[i] / ctotal
        for j in range(1, 10):
            l = ls[j] - (i == j)
            if l < 1:
                continue
            rr = r * l / (ctotal - 1)
            t1 = calc_score(ts + [j])
            if s1 > t1:
                #print(i, j, s1, t1, r, rr)
                result += rr
    print(result)

solve(N, S, T)
