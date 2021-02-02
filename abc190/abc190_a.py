A, B, C = [int(_) for _ in input().split()]

def solve(A: int, B: int, C: int):
    if A == B:
        if C == 0:
            print("Aoki")
        else:
            print("Takahashi")
    elif A < B:
        print("Aoki")
    else:
        print("Takahashi")

solve(A, B, C)
