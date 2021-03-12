# 골드 5레벨        LCS
from sys import stdin

read = stdin.readline
str1 = list(read().strip())
str2 = list(read().strip())
dp = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]

for x in range(1, len(str2) + 1):
    for y in range(1, len(str1) + 1):
        if str1[y - 1] == str2[x - 1]:
            dp[x][y] = dp[x - 1][y - 1] + 1
        else:
            dp[x][y] = max(dp[x - 1][y], dp[x][y - 1])
print(dp[len(str2)][len(str1)])