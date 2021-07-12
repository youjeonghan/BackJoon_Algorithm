# 실버 2레벨    DFS와 BFS

from sys import stdin
from collections import deque

read = stdin.readline

N, M, V = map(int, read().split())
gp = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, read().split())
    gp[s].append(e)
    gp[e].append(s)


def dfs(start):
    result = []
    stack = [start]
    visit = [0] * (N + 1)
    while stack:
        temp = stack.pop()
        if visit[temp] == 0:
            result.append(temp)
            visit[temp] = 1
            for i in sorted(gp[temp], reverse=True):
                if visit[i] == 0:
                    stack.append(i)

    return result


def dfs2(start):
    result = []
    stack = deque([start])
    visit = [0] * (N + 1)
    while stack:
        temp = stack.popleft()
        if visit[temp] == 0:
            result.append(temp)
            visit[temp] = 1
            for i in sorted(gp[temp], reverse=True):
                if visit[i] == 0:
                    stack.appendleft(i)
    return result


visit = [0] * (N + 1)

print(gp)


def dfs3(start):
    print(start, end=" ")
    visit[start] = 1
    for i in gp[start]:
        if visit[i] == 0:
            print("i:", i)
            dfs3(i)


def bfs(start):
    result = []
    que = deque()
    que.append(start)
    visit = [0] * (N + 1)
    while que:
        temp = que.popleft()
        if visit[temp] == 0:
            result.append(temp)
            visit[temp] = 1
            for i in sorted(gp[temp]):
                if visit[i] == 0:
                    que.append(i)
    return result


print(dfs3(V))
# print(*bfs(V))