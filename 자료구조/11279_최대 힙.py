# 실버 2레벨    최대 힙
import heapq as hq
from sys import stdin

N = int(input())
heap = []
for i in range(N):
    t = int(stdin.readline().strip())
    if t != 0:
        hq.heappush(heap, (-t, t))

    else:
        if len(heap) == 0:
            print(0)
        else:
            print(hq.heappop(heap)[1])
