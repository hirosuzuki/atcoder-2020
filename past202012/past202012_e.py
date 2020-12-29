H, W = [int(_) for _ in input().split()]
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

def rot(T, H, W):
    rr = []
    for y in range(W):
        r = []
        for x in range(H):
            r.append(T[x][W - y - 1])
        rr.append(r)
    return rr

def check(S, T):
    SW, SH = len(S[0]), len(S)
    TW, TH = len(T[0]), len(T)
    #print(SW, SH, TW, TH)
    #print(S, T)
    for sy in range(-TH, SH):
        for sx in range(-TW, SW):
            r = True
            for y in range(TH):
                for x in range(TW):
                    if T[y][x] == "#":
                        dy, dx = sy + y, sx + x
                        if dy < 0 or dy >= SH or dx < 0 or dx >= SW:
                            r = False
                            break
                        if S[dy][dx] == "#":
                            r = False
                            break
                if r == False:
                    break
            if r == True:
                #print("!", sy, sx)
                return True
    return False

def solve(H, W, S, T):
    T0 = T
    T1 = rot(T0, H, W)
    T2 = rot(T1, W, H)
    T3 = rot(T2, H, W)
    #print(T0)
    #print(T1)
    #print(T2)
    #print(T3)
    if check(S, T0):
        return True 
    if check(S, T1):
        return True 
    if check(S, T2):
        return True 
    if check(S, T3):
        return True 
    return False

result = solve(H, W, S, T)

if result:
    print("Yes")
else:
    print("No")
