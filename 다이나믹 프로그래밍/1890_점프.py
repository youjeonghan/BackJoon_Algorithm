# 실버 2레벨
# 29분 소요

from sys import stdin

read = stdin.readline

n = int(read())
gp = [list(map(int, read().strip().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for y in range(n):
    for x in range(n):
        t = gp[y][x]
        if t == 0:
            continue
        if y + t < n:
            dp[y + t][x] += dp[y][x]
        if x + t < n:
            dp[y][x + t] += dp[y][x]
print(dp[n - 1][n - 1])


### dfs 풀이 정답은 나오는데 시간초과
# from sys import stdin

# read = stdin.readline

# n = int(read())
# gp = [list(map(int, read().strip().split())) for _ in range(n)]

# global asnwer
# answer = 0


# def dfs(y, x):
#     global answer
#     if y == n - 1 and x == n - 1:
#         answer += 1
#         return

#     if y >= n or x >= n:
#         return

#     dfs(y + gp[y][x], x)
#     dfs(y, x + gp[y][x])


# dfs(0, 0)
# print(answer)