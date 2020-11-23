N = input()
A = [int(_) for _ in input().split()]

m = 0
result = 0

for i in range(2, 1000 + 1):
    r = len([a for a in A if a % i == 0])
    if r > m:
        result = i
        m = r

print(result)
