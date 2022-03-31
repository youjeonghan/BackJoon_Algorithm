# 실버 2레벨
# 45분 소요 (문제를 조금 잘못 이해해서)

from collections import deque

n, m = map(int, input().split())
gp = [list(map(int, input().split())) for _ in range(n)]

# 오른쪽부터시작
dy = [0, 1, 1, 1, 0, -1, -1, -1]
dx = [1, 1, 0, -1, -1, -1, 0, 1]


def bfs(y, x):
    visited = [[0] * m for _ in range(n)]
    deq = deque([[y, x, 0]])
    visited[y][x] = 1

    while deq:
        ty, tx, cnt = deq.popleft()
        for i in range(8):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0:
                if gp[ny][nx] == 1:
                    return cnt + 1

                deq.append([ny, nx, cnt + 1])
                visited[ny][nx] = 1
    return 0


answer = 0
for i in range(n):
    for j in range(m):
        if gp[i][j] == 0:
            answer = max(answer, bfs(i, j))

print(answer)
