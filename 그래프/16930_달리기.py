# 플래티넘 3레벨
# 35분 소요

from sys import stdin
from collections import deque

read = stdin.readline

n, m, k = map(int, read().split())
gp = [list(read().strip()) for _ in range(n)]
check_gp = [[-1] * m for _ in range(n)]
sy, sx, ey, ex = map(int, read().split())
sy, sx, ey, ex = sy - 1, sx - 1, ey - 1, ex - 1
deq = deque([[sy, sx]])
check_gp[sy][sx] = 0


def bfs():
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny, nx = y, x
            for _ in range(k):
                ny += dy[i]
                nx += dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= m or gp[ny][nx] == "#":
                    break
                elif check_gp[ny][nx] == -1:
                    deq.append([ny, nx])
                    check_gp[ny][nx] = check_gp[y][x] + 1
                    if ny == ey and nx == ex:
                        return
                elif check_gp[ny][nx] < check_gp[y][x] + 1:
                    break


bfs()
print(check_gp[ey][ex])