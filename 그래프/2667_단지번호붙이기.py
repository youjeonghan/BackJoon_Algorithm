# 실버 3레벨    단지번호붙이기
from sys import stdin
from collections import deque

read = stdin.readline

N = int(read())
gp = [list(map(int, read().rstrip())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
result = []


def check(y, x):
    if visit[y][x] == 0 and gp[y][x] == 1:
        return 1
    else:
        return 0


def bfs():
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    for y in range(N):
        for x in range(N):
            if check(y, x):
                cnt = 1
                visit[y][x] = 1
                stack = deque([(y, x)])
                while stack:
                    t = stack.popleft()
                    for i in range(0, 4):
                        ty = t[0] + dy[i]
                        tx = t[1] + dx[i]
                        if 0 <= ty < N and 0 <= tx < N and check(ty, tx):
                            cnt += 1
                            visit[ty][tx] = 1
                            stack.append((ty, tx))
                result.append(cnt)


bfs()
result.sort()
print(len(result))
print("\n".join(map(str, (result))))