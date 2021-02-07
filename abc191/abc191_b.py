from typing import List

N, X = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

def solve(N: int, X: int, A: List[int]):
    rs = [n for n in A if n != X]
    print(*rs)

solve(N, X, A)

