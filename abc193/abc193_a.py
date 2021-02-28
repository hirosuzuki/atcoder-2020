A, B = [int(_) for _ in input().split()]

def solve(A: int, B: int):
    result = (A - B) / A * 100
    print(result)

solve(A, B)
