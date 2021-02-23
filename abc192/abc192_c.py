N, K = [int(_) for _ in input().split()]

def solve(N: int, K: int):

    def g1(x: int) -> int:
        return int("".join(sorted(str(x), reverse=True)))

    def g2(x: int) -> int:
        return int("".join(sorted(str(x), reverse=False)))

    def f(x: int) -> int:
        return g1(x) - g2(x)

    n = N
    for _ in range(K):
        n = f(n)

    print(n)

solve(N, K)