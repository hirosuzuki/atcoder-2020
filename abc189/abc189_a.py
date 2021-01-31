C = input()

def solve(C: str):
    if C[0] == C[1] == C[2]:
        print("Won")
    else:
        print("Lost")

solve(C)
