from typing import List

N = int(input())
AB = [[int(_) for _ in input().split()] for _ in range(N)]

def solve(N: int, AB: List[List[int]]):
    s, t = sum(a for a, _ in AB), 0
    ab = sorted(AB, key=lambda x:x[0]*2+x[1], reverse=True)
    result = 0
    while s >= t:
        s -= ab[result][0]
        t += ab[result][0] + ab[result][1]
        result += 1
    print(result)

solve(N, AB)
