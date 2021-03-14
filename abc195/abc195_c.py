import sys

sys.setrecursionlimit(100000)

N = int(input())

def solve(N: int):

    def calc(N: int) -> int:
        if N < 1000:
            return 0
        for i in range(1, 10):
            m = 1000 ** i
            if N < m * 1000:
                r = (N - m + 1) * i + calc(m - 1)
                #print("*", N, r)
                return r

        return -1

    print(calc(N))

solve(N)