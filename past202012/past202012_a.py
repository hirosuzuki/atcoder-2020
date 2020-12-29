S = input()

def solve(S):
    if "ooo" in S:
        return "o"
    if "xxx" in S:
        return "x"
    return "draw"

result = solve(S)

print(result)
