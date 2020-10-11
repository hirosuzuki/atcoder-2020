H, W = [int(_) for _ in input().split()]
S = [input() for _ in range(H)]

result = 0
for y in range(H):
    for x in range(W):
        if S[y][x] == ".":
            result += (x + 1 < W and S[y][x + 1] == ".")
            result += (y + 1 < H and S[y + 1][x] == ".")

print(result)
