A, B = [int(_) for _ in input().split()]

def solve(A: int, B: int):
    C = A + B
    if C >= 15 and B >= 8:
        print(1)
    elif C >= 10 and B >= 3:
        print(2)
    elif C >= 3:
        print(3)
    else:
        print(4)

solve(A, B)
