# 실버 2레벨    유기농 배추
T = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(y, x):
    gp[y][x] = 0
    stack = [(y, x)]
    while stack:
        target = stack.pop()
        for i in range(4):
            a = target[0] + dy[i]
            b = target[1] + dx[i]

            if 0 <= a < N and 0 <= b < M and gp[a][b] == 1:
                gp[a][b] = 0
                stack.append((a, b))


for i in range(T):
    M, N, K = map(int, input().split())
    gp = [[0 for x in range(M)] for y in range(N)]
    cnt = 0

    for j in range(K):
        x, y = map(int, input().split())
        gp[y][x] = 1

    for y in range(N):
        for x in range(M):
            if gp[y][x] == 1:
                dfs(y, x)
                cnt += 1
    print(cnt)