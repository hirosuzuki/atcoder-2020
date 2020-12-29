N = int(input())
S = input()

def solve(N, S):
    result = []
    for c in S:
        if c in result:
            result.remove(c)
        result.append(c)
    return "".join(result)

result = solve(N, S)

print(result)
