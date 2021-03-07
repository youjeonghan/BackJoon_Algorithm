# 실버 1레벨        숨바꼭질
from sys import stdin
from collections import deque


def bfs():
    que = deque()
    cnt = 0
    que.append((N, cnt))
    while que:
        t = que.popleft()
        if t[0] == K:
            return t[1]

        cnt = t[1] + 1
        if t[0] + 1 <= 100000 and not gp[t[0] + 1]:
            gp[t[0] + 1] = True
            que.append((t[0] + 1, cnt))

        if t[0] * 2 <= 100000 and not gp[t[0] * 2]:
            gp[t[0] * 2] = True
            que.append((t[0] * 2, cnt))

        if t[0] - 1 >= 0 and not gp[t[0] - 1]:
            gp[t[0] - 1] = True
            que.append((t[0] - 1, cnt))

    return cnt


N, K = map(int, stdin.readline().split())
gp = [False] * 100001
print(bfs())