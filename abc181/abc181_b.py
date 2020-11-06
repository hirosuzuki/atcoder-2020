N = int(input())
AB = [[int(_) for _ in input().split()] for _ in range(N)]

result = sum([(a + b) * (b - a + 1) // 2 for a, b in AB])

print(result)
