N = int(input())
X = [int(x) for x in input().split()]

from math import sqrt

result1 = sum([abs(e) for e in X])
result2 = sqrt(sum([e*e for e in X]))
result3 = max([abs(e) for e in X])

print(result1)
print(result2)
print(result3)
