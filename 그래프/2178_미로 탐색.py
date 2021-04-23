# 실버 1레벨    미로 탐색
# 그래프 bfs
from sys import stdin
from collections import deque

read = stdin.readline
N, M = map(int, read().split())
gp = [[0] * (M + 1)]
for _ in range(N):
    gp.append([0] + list(map(int, read().rstrip())))

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]
cnt = 0


def bfs():
    que = deque()
    que.append([1, 1, 1])  # y,x,cnt
    visit = [[0] * (M + 1) for _ in range(N + 1)]
    visit[1][1] = 1
    while que:
        t = que.popleft()
        if [t[0], t[1]] == [N, M]:
            return t[2]
        for i in range(4):
            y = t[0] + dy[i]
            x = t[1] + dx[i]
            if y <= N and x <= M and gp[y][x] == 1 and visit[y][x] == 0:
                que.append([y, x, t[2] + 1])
                visit[y][x] = 1


print(bfs())