N = int(input())
A = [int(_) for _ in input().split()]

def solve(N, A):
    s = sum(A)
    i, j = 0, 0
    r = 0
    f = True
    result = s
    while f:
        f = False
        while j < N and r < s / 2:
            r += A[j]
            j += 1
            f = True
            rr = abs(s - r - r)
            result = min(result, rr)
        while i < N and r >= s / 2:
            r -= A[i]
            i += 1
            f = True
            rr = abs(s - r - r)
            result = min(result, rr)
    return result

print(solve(N, A))
