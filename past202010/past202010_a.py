A, B, C = [int(_) for _ in input().split()]

xs = sorted([(A, "A"), (B, "B"), (C, "C")])
result = xs[1][1]

print(result)
