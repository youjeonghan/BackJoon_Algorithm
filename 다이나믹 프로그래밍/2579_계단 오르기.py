# 실버 3레벨    계단 오르기
from sys import stdin

read = stdin.readline

n = int(read())
v = [0]
for i in range(n):
    v.append(int(read()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    one = dp[i - 2] if i - 2 >= 0 else 0

    two = dp[i - 3] if i - 3 >= 0 else 0
    two += v[i - 1] if i - 1 >= 0 else 0

    dp[i] = max(one, two) + v[i]
print(dp[n])
