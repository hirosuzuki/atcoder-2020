N, M = [int(_) for _ in input().split()]
ABC = [[int(_) for _ in input().split()] for _ in range(M)]

def solve0(N, M, ABC):
    result = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            r = 0
            for a, b, c in ABC:
                if (i == a and j == b) or (i == b and j == c) or (i == a and j == c):
                    r += 1
            #print(i, j, r)
            result = max(result, r)
    return result

def solve1(N, M, ABC):
    from collections import defaultdict
    cs = defaultdict(int)
    for a, b, c in ABC:
        cs[(a, b)] += 1
        cs[(b, c)] += 1
        cs[(a, c)] += 1
    result = max(cs.values())
    #print(cs)
    return result

def solve(N, M, ABC):
    bs = [(1<<(a-1))|(1<<(b-1))|(1<<(c-1)) for a, b, c in ABC]
    bs1 = [((1<<(a-1))|(1<<(b-1)), c) for a, b, c in ABC]
    bs2 = [((1<<(b-1))|(1<<(c-1)), a) for a, b, c in ABC]
    bs3 = [((1<<(a-1))|(1<<(c-1)), b) for a, b, c in ABC]
    result = 0
    for i in range(2**N):
        if any((i & b) == b for b in bs):
            continue        
        rs = set()
        for b, k in bs1:
            if (i & b) == b:
                rs.add(k)
        for b, k in bs2:
            if (i & b) == b:
                rs.add(k)
        for b, k in bs3:
            if (i & b) == b:
                rs.add(k)
        r = len(rs)
        #print(bin(i), r, rs)
        result = max(result, r)
    return result

result = solve(N, M, ABC)

print(result)
