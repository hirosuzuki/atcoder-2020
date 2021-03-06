from typing import List, Tuple, Dict

from sys import setrecursionlimit
setrecursionlimit(100000)

N = int(input())
XYR = [[int(_) for _ in input().split()] for _ in range(N)]

def solve(N: int, XYR: List[List[int]]):

    ns: List[int] = list(range(N))
    na: Dict[int, Tuple[int, int, int, int]] = {}

    def alloc(n: int, area: Tuple[int, int, int, int]):
        x, y, r = XYR[n] 
        if area[0] <= x < area[2] and area[1] <= y < area[3]:
            w = area[2] - area[0]
            h = area[3] - area[1]
            l = w * h
            if r >= l:
                na[n] = area
            else:
                h = r // w
                h = max(h, 1)
                y0 = min(area[3] - h, y)
                a = (area[0], y0, area[2], y0 + h)
                if a[0] <= x < a[2] and a[1] <= y < a[3]:
                    na[n] = a
                else:
                    raise Exception
        else:
            raise Exception

    def div(ns: List[int], area: Tuple[int, int, int, int]):

        if len(ns) == 2:
            xm = (area[0] + area[2]) // 2
            ym = (area[1] + area[3]) // 2
            xns = sorted(ns, key=lambda i:XYR[i][0])
            yns = sorted(ns, key=lambda i:XYR[i][1])
            if XYR[xns[0]][0] < xm < XYR[xns[1]][0]:
                a0 = (area[0], area[1], xm, area[3])
                a1 = (xm, area[1], area[2], area[3])
                alloc(xns[0], a0)
                alloc(xns[1], a1)
                return
            elif XYR[yns[0]][1] < ym < XYR[yns[1]][1]:
                a0 = (area[0], area[1], area[2], ym)
                a1 = (area[0], ym, area[2], area[3])
                alloc(yns[0], a0)
                alloc(yns[1], a1)
                return
            else:
                dx = XYR[xns[1]][0] - XYR[xns[0]][0]
                dy = XYR[yns[1]][1] - XYR[yns[0]][1]
                if dx > dy:
                    if xm < XYR[xns[0]][0]:
                        xm = XYR[xns[1]][0]
                        a0 = (area[0], area[1], xm, area[3])
                        a1 = (xm, area[1], area[2], area[3])
                        alloc(xns[0], a0)
                        alloc(xns[1], a1)
                        return
                    if XYR[xns[1]][0] < xm:
                        xm = XYR[xns[0]][0] + 1
                        a0 = (area[0], area[1], xm, area[3])
                        a1 = (xm, area[1], area[2], area[3])
                        alloc(xns[0], a0)
                        alloc(xns[1], a1)
                        return
                else:
                    if ym < XYR[yns[0]][1]:
                        ym = XYR[yns[1]][1]
                        a0 = (area[0], area[1], area[2], ym)
                        a1 = (area[0], ym, area[2], area[3])
                        alloc(yns[0], a0)
                        alloc(yns[1], a1)
                        return
                    if XYR[yns[1]][1] < ym:
                        ym = XYR[yns[0]][1] + 1
                        a0 = (area[0], area[1], area[2], ym)
                        a1 = (area[0], ym, area[2], area[3])
                        alloc(yns[0], a0)
                        alloc(yns[1], a1)
                        return

        if area[2] - area[0] > area[3] - area[1]:
            m = (area[0] + area[2]) // 2
            a0 = (area[0], area[1], m, area[3])
            a1 = (m, area[1], area[2], area[3])
        else:
            m = (area[1] + area[3]) // 2
            a0 = (area[0], area[1], area[2], m)
            a1 = (area[0], m, area[2], area[3])
        ns0: List[int] = []
        ns1: List[int] = []
        for i in ns:
            x, y, _ = XYR[i]
            if a0[0] <= x < a0[2] and a0[1] <= y < a0[3]:
                ns0.append(i)
            elif a1[0] <= x < a1[2] and a1[1] <= y < a1[3]:
                ns1.append(i)
            else:
                raise Exception

        if len(ns0) > 1:
            div(ns0, a0)
        else:
            if len(ns0) == 1:
                n = ns0[0]
                alloc(n, a0)

        if len(ns1) > 1:
            div(ns1, a1)
        else:
            if len(ns1) == 1:
                n = ns1[0]
                alloc(n, a1)

    div(ns, (0, 0, 10000, 10000))
    for i in range(N):
        print(*na[i])

solve(N, XYR)
