V, T, S, D = [int(_) for _ in input().split()]

def solve(V: int, T: int, S: int, D: int):
    t = V * T
    s = V * S
    if t <= D <= s:
        print("No")
    else:
        print("Yes")

solve(V, T, S, D)
