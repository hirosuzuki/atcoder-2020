N = int(input())
AB = [[int(_) for _ in input().split()] for _ in range(N)]

def calc(N, AB) -> bool:
    for i in range(0, N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                x0, y0, = AB[i]
                x1, y1, = AB[j]
                x2, y2, = AB[k]
                if (x1 - x0) * (y2 - y0) == (x2 - x0) * (y1 - y0):
                    return True
    return False

result = ["No", "Yes"][calc(N, AB)]

print(result)

