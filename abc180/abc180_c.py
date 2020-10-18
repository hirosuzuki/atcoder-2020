N = int(input())

from math import sqrt

result = []
for i in range(1, int(sqrt(N)) + 1):
    if N % i == 0:
        result.append(i)
        j = N // i
        if j != i:
            result.append(N // i)

result.sort()
print(*result, sep="\n")

