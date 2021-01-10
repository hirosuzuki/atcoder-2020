from typing import List

N = int(input())
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]

def solve(N: int, A: List[int], B: List[int]):
    result = sum(a * b for a, b in zip(A, B))
    if result == 0:
        print("Yes")
    else:
        print("No")

solve(N, A, B)
