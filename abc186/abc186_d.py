from typing import List

N = int(input())
A = [int(_) for _ in input().split()]

def solve0(N: int, A: List[int]):
    result = 0
    xs = sorted(A)
    for i in range(N):
        for j in range(i + 1, N):
            result += (xs[j] - xs[i])
    print(result)


def solve(N: int, A: List[int]):
    xs = sorted(A)
    result = 0
    dp: List[int] = [0] * (N + 1)
    for i in range(1, N):
        dp[i] = (xs[i] - xs[i - 1]) * i + dp[i - 1]
        result += dp[i]
    print(result)

solve(N, A)
