N = int(input())

def solve(N):
    if N == 0:
        return "0"
    cs = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    x = N
    while x:
        y = x % 36
        result = cs[y] + result
        x = x // 36
    return result

result = solve(N)

print(result)
