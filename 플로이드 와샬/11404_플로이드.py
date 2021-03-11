# 골드 4레벨        플로이드
# 플로이드 와샬 알고리즘
from sys import stdin, maxsize

read = stdin.readline

n = int(read())
m = int(read())

graph = [[maxsize] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    s, e, w = map(int, read().split())
    if graph[s][e] > w:
        graph[s][e] = w


def floyd():
    for cross in range(1, n + 1):
        for s in range(1, n + 1):
            if cross == s:
                continue
            for e in range(1, n + 1):
                if cross == e or s == e:
                    continue

                if graph[s][e] > graph[s][cross] + graph[cross][e]:
                    graph[s][e] = graph[s][cross] + graph[cross][e]


floyd()
for s in range(1, n + 1):
    for e in range(1, n + 1):
        if graph[s][e] == maxsize:
            print(0, end=" ")
        else:
            print(graph[s][e], end=" ")
    print()