# 골드 5레벨
# 다익스트라 알고리즘

from sys import stdin
from collections import defaultdict
import heapq as hq

read = stdin.readline

city = int(read())
bus = int(read())

vertex = {i: float("inf") for i in range(1, city + 1)}
edge = defaultdict(list)
heap = []

for _ in range(bus):
    s, e, w = map(int, read().split())
    edge[s].append((e, w))


start, end = map(int, read().split())

vertex[start] = 0
hq.heappush(heap, (0, start))

while heap:
    w, node = hq.heappop(heap)
    if vertex[node] < w:
        continue
    for n_v, n_w in edge[node]:
        if vertex[n_v] > w + n_w:
            vertex[n_v] = w + n_w
            hq.heappush(heap, (vertex[n_v], n_v))

print(vertex[end])
