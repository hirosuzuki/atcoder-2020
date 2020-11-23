N = int(input())
A = [int(_) for _ in input().split()]

def resolve(N, A):
    ms = [0] * N
    ds = [0] * N

    d = 0
    m = 0
    for i in range(N):
        d += A[i]
        m = max(m, d)
        ds[i] = d
        ms[i] = m

    #print(ds, ms)
    
    x = 0
    result = 0
    for i in range(N):
        m = x + ms[i]
        x += ds[i]
        result = max(result, m)

    return result

result = resolve(N, A)
print(result)
