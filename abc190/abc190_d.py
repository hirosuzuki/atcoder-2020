N = int(input())

def solve(N: int):
    result = 0
    m = 2 * N
    for i in range(1, m):
        if i * i > m:
            break
        if m % i > 0:
            continue
        n = m // i
        if (m / n + 1 - n) % 2 == 0:
            # print(i)
            result += 2

    print(result)

solve(N)
