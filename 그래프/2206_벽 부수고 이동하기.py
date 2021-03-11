# 골드 4레벨        벽 부수고 이동하기
from collections import deque
from sys import stdin

read = stdin.readline

N, M = map(int, read().split())

graph = [list((map(int, read().strip()))) for _ in range(N)]
visit = [[[0, 0] for _ in range(M)] for _ in range(N)]  # [벽안부수고 온적있을때, 벽 부수고 온적 있을때]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    que = deque()
    que.append((0, 0, 1, 0))
    visit[0][0] = [1, 1]

    while que:
        t = que.popleft()
        for i in range(4):
            x = t[0] + dx[i]
            y = t[1] + dy[i]
            # print(x, y)
            if not 0 <= x < N or not 0 <= y < M:
                continue

            if t[3] == 0:  # 벽아직 안부시고옴
                if visit[x][y][0] == 0 and graph[x][y] == 0:  # 안부순상태 and 부실필요 X (길)
                    que.append((x, y, t[2] + 1, 0))
                    visit[x][y][0] = t[2] + 1
                elif visit[x][y][1] == 0 and graph[x][y] == 1:  # 안부순상태 and 부실필요 O (벽)
                    que.append((x, y, t[2] + 1, 1))
                    visit[x][y][1] = t[2] + 1

            if t[3] == 1 and visit[x][y][1] == 0 and graph[x][y] == 0:  # 벽 부시고옴
                que.append((x, y, t[2] + 1, 1))
                visit[x][y][1] = t[2] + 1

            if visit[N - 1][M - 1][0] or visit[N - 1][M - 1][1]:
                return


bfs()
a, b = visit[N - 1][M - 1]
if a == b == 0:
    print(-1)
elif a > 0 and b > 0:
    print(min(a, b))
else:
    print(max(a, b))
