A, B = input().split()

def solve(A: str, B: str):
    def calc(x: str) -> int:
        return sum(int(c) for c in x)
    print(max(calc(A), calc(B)))

solve(A, B)
