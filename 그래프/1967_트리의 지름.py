# 골드 4레벨        트리의 지름
from sys import stdin, maxsize
from collections import deque

read = stdin.readline
n = int(read())
graph = [[] for i in range(n + 1)]

for _ in range(n - 1):
    s, e, w = map(int, read().split())
    graph[s].append((e, w))
    graph[e].append((s, w))


def bfs(start):
    que = deque()
    que.append(start)
    visit = [-1] * (n + 1)
    visit[start] = 0
    max_node = 1
    while que:
        s = que.popleft()
        for e, w in graph[s]:
            if visit[e] == -1:
                que.append(e)
                visit[e] = visit[s] + w

                if visit[max_node] < visit[e]:
                    max_node = e
    # print(visit)
    return max_node, visit[max_node]


start, long = bfs(1)
result, long = bfs(start)
print(long)
