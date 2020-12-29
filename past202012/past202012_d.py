N = int(input())
S = [input() for _ in range(N)]

def solve(N, S: str):
    xs = []
    for s in S:
        s0 = s.lstrip("0")
        xs.append((len(s0), s0, len(s0)-len(s), s))
    xs.sort()
    for x in xs:
        print(x[3])

solve(N, S)
