from typing import List

N = int(input())

def solve(N: int):
    L = 100000
    cs: List[int] = [0] * (L + 1)
    r = 0
    for i in range(2, L + 1):
        if cs[i]:
            continue
        x = i * i
        while x <= N:
            if x <= L:
                cs[x] = 1
            r += 1
            x *= i
    print(N - r)

solve(N)
