M, H = [int(_) for _ in input().split()]

def solve(M: int, H: int):
    if H % M == 0:
        print("Yes")
    else:
        print("No")

solve(M, H)
