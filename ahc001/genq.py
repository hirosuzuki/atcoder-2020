from random import random, randint, randrange
from typing import List, Tuple

N = round(50 * 4 **random())
XY: List[Tuple[int, int]] = []
Q: List[int] = [0]

for _ in range(N):
    while True:
        x, y = randint(0, 9999), randint(0, 9999)
        if (x, y) not in XY:
            break
    XY.append((x, y))
    while True:
        q = randint(1, 99999999)
        if q not in Q:
            break
    Q.append(q)

Q.sort()
R = [Q[i + 1] - Q[i] for i in range(N)]

print(N)
for i in range(N):
    print(*XY[i], R[i])
