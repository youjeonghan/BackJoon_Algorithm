# 실버 1레벨
# 다시 풀기

t = int(input())
dp = [-1] * 10_001

dp[1] = 1
dp[2] = 2
dp[3] = 3


def find_dp(n):
    if dp[n] == -1:
        dp[n] = dp[n - 1] + dp[n - 2] + dp[n - 3]
    return dp[n]


for _ in range(t):
    print(find_dp(int(input())))