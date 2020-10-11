N = int(input())
P = [int(_) for _ in input().split()]

r = 0
xs = [0] * 200001
for i in range(N):
    xs[P[i]] = 1
    while xs[r] == 1:
        r += 1
    print(r)
