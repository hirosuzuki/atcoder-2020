X, Y = [int(_) for _ in input().split()]

def solve(X: int, Y: int):
    if abs(X - Y) < 3:
        print("Yes")
    else:
        print("No")

solve(X, Y)
