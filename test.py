# 골드 4레벨        웜홀
# 벨만 포드 알고리즘

from sys import stdin, maxsize
from collections import defaultdict

# maxsize = 2147483647
read = stdin.readline
t = int(read())


def bellman(graph):
    vertex = defaultdict(lambda: maxsize)
    # vertex = [maxsize for _ in range(N + 1)]
    for i in range(N - 1):
        for s in graph:
            for e in graph[s]:
                if vertex[e] > vertex[s] + graph[s][e]:
                    vertex[e] = vertex[s] + graph[s][e]

    for s in graph:
        for e in graph[s]:
            if vertex[e] > vertex[s] + graph[s][e]:
                return -1  # 음의 사이클 존재

    return 1


for _ in range(t):
    graph = defaultdict(lambda: defaultdict(lambda: maxsize))

    N, M, W = map(int, read().split())

    for _ in range(M):
        S, E, T = map(int, read().split())
        if graph[S][E] > T:
            graph[S][E] = T
        if graph[S][E] > T:
            graph[E][S] = T

    for _ in range(W):
        S, E, T = map(int, read().split())
        if graph[S][E] > -T:
            graph[S][E] = -T

    result = "NO"
    if bellman(graph) == -1:
        result = "YES"
    print(result)