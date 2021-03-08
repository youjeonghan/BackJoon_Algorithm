# 실버 1레벨        최소 힙
import heapq as hq
from sys import stdin

heap = []
result = []

N = int(stdin.readline())

for _ in range(N):
    num = int(stdin.readline())
    if num != 0:
        hq.heappush(heap, num)

    else:
        if heap:
            result.append(hq.heappop(heap))
        else:
            result.append(0)

for i in result:
    print(i)