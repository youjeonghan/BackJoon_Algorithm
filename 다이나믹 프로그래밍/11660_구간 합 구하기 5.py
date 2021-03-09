# 실버 1레벨        구간 합 구하기 5
# 풀이 보고 풀었음 나중에 다시 풀어보기
# 다시
from sys import stdin

read = stdin.readline

N, M = map(int, read().split())
_map = [list(map(int, read().split())) for _ in range(N)]
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + _map[i - 1][j - 1] - dp[i - 1][j - 1]

for i in range(M):
    x1, y1, x2, y2 = map(int, read().split())
    print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])
