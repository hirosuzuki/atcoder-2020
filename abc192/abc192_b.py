S = input()

def solve(S: str):
    if S[::2].lower() == S[::2] and S[1::2].upper() == S[1::2]:
        print("Yes")
    else:
        print("No")

solve(S)