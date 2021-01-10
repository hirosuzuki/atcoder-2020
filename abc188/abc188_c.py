from typing import List

N = int(input())
A = [int(_) for _ in input().split()]

def solve(N: int, A: List[int]):
    l = 2**N
    xs0 = sorted(enumerate(A[:l//2]), key=lambda x:x[1])
    xs1 = sorted(enumerate(A[l//2:]), key=lambda x:x[1])
    if xs0[-1][1] < xs1[-1][1]:
        result = xs0[-1][0] + 1
    else:
        result = xs1[-1][0] + 1 + l//2
    print(result)

solve(N, A)
