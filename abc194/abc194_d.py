N = int(input())

def solve(N: int):
    result = 0
    for i in range(1, N):
        r = N / (N - i)
        result += r
    print(result)

solve(N)
