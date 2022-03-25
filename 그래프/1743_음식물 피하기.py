# 실버 1레벨
answer = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(y, x):
    global answer
    stack = [(y, x)]
    visited[y][x] = 1
    cnt = 1
    while stack:
        y, x = stack.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and gp[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                cnt += 1
                stack.append((ny, nx))
    answer = max(answer, cnt)


n, m, k = map(int, input().split())
gp = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
for _ in range(k):
    y, x = map(int, input().split())
    gp[y - 1][x - 1] = 1

for y in range(n):
    for x in range(m):
        if visited[y][x] == 0 and gp[y][x] == 1:
            bfs(y, x)

print(answer)