from typing import List, Tuple
import sys
sys.setrecursionlimit(20000)

N = int(input())
A = [int(_) for _ in input().split()]

def solve(N: int, A: List[int]):
    def findmin(A: List[int], l: int, r: int) -> Tuple[int, int]:
        min_index, min_value = l, A[l]
        for i in range(l + 1, r):
            v = A[i]
            if v < min_value:
                min_value = v
                min_index = i
        return min_index, min_value
    def calc(A: List[int], l: int, r: int) -> int:
        if l >= r:
            return 0        
        i, v = findmin(A, l, r)
        t = v * (r - l)
        return max(t, calc(A, l, i), calc(A, i + 1, r))
    print(calc(A, 0, N))

solve(N, A)
