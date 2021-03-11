# 골드 4레벨        웜홀
# 벨만 포드 알고리즘

from sys import stdin, maxsize
from collections import defaultdict

read = stdin.readline
t = int(read())


def bellman(graph):
    vertex = defaultdict(lambda: maxsize)
    # vertex = [maxsize for _ in range(N + 1)]
    for i in range(N - 1):
        for s in range(1, N + 1):
            for e, t in graph[s]:
                if vertex[e] > vertex[s] + t:
                    vertex[e] = vertex[s] + t

    for s in range(1, N + 1):
        for e, t in graph[s]:
            if vertex[e] > vertex[s] + t:
                return -1  # 음의 사이클 존재

    return 1


for _ in range(t):

    N, M, W = map(int, read().split())
    # graph = defaultdict(dict)
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        S, E, T = map(int, read().split())
        graph[S].append((E, T))
        graph[E].append((S, T))

    for _ in range(W):
        S, E, T = map(int, read().split())
        graph[S].append((E, -T))

    result = "NO"
    if bellman(graph) == -1:
        result = "YES"
    print(result)