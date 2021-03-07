from typing import List

N = int(input())
A = [int(_) for _ in input().split()]

def solve(N: int, A: List[int]):
    result = N * sum([x*x for x in A]) - sum(A)**2
    print(result)

solve(N, A)
