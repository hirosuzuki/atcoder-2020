A, B, W = [int(_) for _ in input().split()]

def solve(A: int, B: int, W: int):
    rmax = (W * 1000) // A
    rmin = (W * 1000 + B - 1) // B
    while 1:
        if rmax * A <= W * 1000 <= rmax * B:
            break
        if rmax * B < W * 1000:
            break
        rmax -= 1
    while 1:
        if rmin * A <= W * 1000 <= rmin * B:
            break
        if rmin * A > W * 1000:
            break
        rmin += 1
    if rmin <= rmax:
        print(rmin, rmax)
    else:
        print("UNSATISFIABLE")

solve(A, B, W)
