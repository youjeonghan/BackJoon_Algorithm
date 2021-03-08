# 골드 5레벨        이중 우선순위 큐
from sys import stdin
import heapq as hq

read = stdin.readline
T = int(read())
for _ in range(T):
    k = int(read())
    min_h = []
    max_h = []
    check = [0] * 1000001
    for i in range(k):
        c = read().split()
        if c[0] == "I":
            hq.heappush(min_h, (int(c[1]), i))
            hq.heappush(max_h, (-int(c[1]), i))
            check[i] = 1

        elif c[1] == "-1":
            while min_h and check[min_h[0][1]] == 0:
                hq.heappop(min_h)

            if min_h and check[min_h[0][1]] == 1:
                check[min_h[0][1]] = 0
                hq.heappop(min_h)

        else:
            while max_h and check[max_h[0][1]] == 0:
                hq.heappop(max_h)

            if max_h and check[max_h[0][1]] == 1:
                check[max_h[0][1]] = 0
                hq.heappop(max_h)

    while min_h and check[min_h[0][1]] == 0:
        hq.heappop(min_h)

    while max_h and check[max_h[0][1]] == 0:
        hq.heappop(max_h)

    if max_h and min_h:
        print(f"{-max_h[0][0]} {min_h[0][0]}")
    else:
        print("EMPTY")