# 실버 3레벨
# 다시 풀기

n = int(input())
gp = [list(map(str, input())) for _ in range(n)]

global answer
answer = 0


def check(y, x):
    global answer
    global cnt
    standard = gp[y][x]

    def bfs(dy, dx):
        global cnt
        ny, nx = y + dy, x + dx
        while 0 <= ny < n and 0 <= nx < n:
            if gp[ny][nx] == standard:
                cnt += 1
                ny += dy
                nx += dx
            else:
                break

    cnt = 1
    bfs(0, 1)
    bfs(0, -1)
    answer = max(answer, cnt)
    cnt = 1
    bfs(1, 0)
    bfs(-1, 0)
    answer = max(answer, cnt)


for y in range(n):
    for x in range(n - 1):
        gp[y][x], gp[y][x + 1] = gp[y][x + 1], gp[y][x]
        check(y, x)
        check(y, x + 1)
        gp[y][x], gp[y][x + 1] = gp[y][x + 1], gp[y][x]

        if y != n - 1:
            gp[y][x], gp[y + 1][x] = gp[y + 1][x], gp[y][x]
            check(y, x)
            check(y + 1, x)
            gp[y][x], gp[y + 1][x] = gp[y + 1][x], gp[y][x]

print(answer)
