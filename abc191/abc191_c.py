from typing import List

H, W = [int(_) for _ in input().split()]
S = [input() for _ in range(H)]

def solve(H: int, W: int, S: List[str]):
    result = 0
    t = {
        "....": 0,
        "...#": 1,
        "..#.": 1,
        "..##": 0,
        ".#..": 1,
        ".#.#": 0,
        ".##.": 2,
        ".###": 1,
        "#...": 1,
        "#..#": 2,
        "#.#.": 0,
        "#.##": 1,
        "##..": 0,
        "##.#": 1,
        "###.": 1,
        "####": 0,
    }
    for y in range(H - 1):
        for x in range(W - 1):
            cs = S[y][x:x+2] + S[y+1][x:x+2]
            result += t[cs]
    print(result)

solve(H, W, S)

