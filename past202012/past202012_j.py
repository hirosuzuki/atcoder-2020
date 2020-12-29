S = input()
N = int(input())

#import sys
#sys.setrecursionlimit(70000)
import bisect

def solve(S, N):
    lens = []
    r = 0
    for i, c in enumerate(S):
        if c >= "a":
            lens.append(r)
            r += 1
        else:
            lens.append(r)
            r += r * int(c)
        if r >= N:
            break

    #print(lens)

    n = N - 1
    for i in range(len(lens) - 1, -1, -1):
        if S[i] < "a":
            n = n % lens[i]
        else:
            if lens[i] == n:
                return S[i]
        #print(i, n, lens[i], S[i])

    result = ""
    
    return result

result = solve(S, N)

print(result)
