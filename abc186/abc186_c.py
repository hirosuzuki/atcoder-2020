N = int(input())

def solve(N: int):
    result = 0
    for i in range(1, N + 1):
        if ("7" not in str(i)) and ("7" not in "%o" % i):
            result += 1
    print(result)

solve(N)
