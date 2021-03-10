# 골드 5레벨        최단경로
import heapq as hq
from collections import deque, defaultdict
from sys import stdin, maxsize

read = stdin.readline

V, E = map(int, read().split())
K = int(read())
edge = defaultdict(list)
vertex = {i: maxsize for i in range(1, V + 1)}


for _ in range(E):
    u, v, w = map(int, read().split())
    edge[u].append((v, w))

vertex[K] = 0
order = 1
visit = [0] * (V + 1)
heap = []
hq.heappush(heap, (0, K))
while heap:
    node = hq.heappop(heap)
    visit[node[1]] = 1
    for v, w in edge[node[1]]:
        if vertex[v] > node[0] + w:
            vertex[v] = node[0] + w
            if not visit[v]:
                hq.heappush(heap, (vertex[v], v))


for k, v in vertex.items():
    if v == maxsize:
        print("INF")
    else:
        print(v)