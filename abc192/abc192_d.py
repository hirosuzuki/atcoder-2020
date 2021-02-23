X = input()
M = int(input())

def solve(X: str, M: int):
    xs = [int(_) for _ in X]
    d = max(xs) + 1
    rmin = d
    rmax = M + 1

    def check(n: int) -> bool:
        x = 0
        for d in xs:
            x = x * n + d
        return x <= M

    if check(d) == False:
        print(0)
        return

    if len(xs) == 1:
        print(1)
        return

    while rmin < rmax - 1:
        r = (rmin + rmax) // 2
        if check(r):
            rmin = r
        else:
            rmax = r

    m = min(M, rmin)
    result = max(m - d + 1, 0)
    print(result)

solve(X, M)
