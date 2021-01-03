from typing import List, Set

N = int(input())
S = [input() for _ in range(N)]

def solve(N: int, S: List[str]):
    ss: Set[str] = set()
    for s in S:
        ss.add(s)
    for s in S:
        if s in ss and ("!" + s) in ss:
            print(s)
            return
    print("satisfiable")

solve(N, S)
