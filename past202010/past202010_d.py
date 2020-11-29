N = int(input())
S = input()

def solve(N, S):
    xs = S.split("#")
    cs = [len(x) for x in xs]
    m = max(cs)
    X = cs[0] + max(m - cs[0] - cs[-1], 0)
    Y = cs[-1]
    return X, Y

print(*solve(N, S))
