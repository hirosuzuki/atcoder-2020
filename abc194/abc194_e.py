from typing import List

N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

def solve(N: int, M: int, A: List[int]):
    ns = [0] * 1500001

    r = 0
    result = 1500001

    def append(n: int):
        nonlocal r
        ns[n] += 1
        while ns[r] > 0:
            r += 1

    def remove(n: int):
        nonlocal r
        ns[n] -= 1
        if ns[n] == 0 and n < r:
            r = n

    for i in range(M):
        append(A[i])
    result = min(result, r)
    #print("*", r, ns[:10])

    for i in range(N - M):
        if A[i + M] != A[i]:
            append(A[i + M])
            remove(A[i])
            result = min(result, r)
        #print("*", r, ns[:10])

    print(result)

solve(N, M, A)
