X, Y = [int(_) for _ in input().split()]

import math

def solve(X, Y):
    if Y == 0:
        print("ERROR")
        return
    print("%.2f" % (math.floor(X * 100/ Y) / 100))

solve(X, Y)
