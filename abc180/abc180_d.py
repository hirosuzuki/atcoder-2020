X, Y, A, B = [int(x) for x in input().split()]

n = X
k = 0
while True:
    a, b = n * A, n + B
    if a >= Y or b >= Y:
        break
    if a > b:
        break
    n = a
    k += 1

#print(k)

if Y - n - 1 >= B:
    m = (Y - n - 1) // B
    k += m

result = k

print(result)
