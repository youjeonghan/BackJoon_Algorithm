# 실버 5레벨        Four Squares
from sys import stdin, maxsize

N = int(input())
dp = [0, 1]

j = 1
for i in range(2, N + 1):
    min_value = 4
    if ((j + 1) ** 2) <= i:
        j += 1
    min_value = min(min_value, dp[i - (j ** 2)])

    dp.append(min_value + 1)

print(dp[1 ** 2])
print(dp[27 ** 2])
print(dp[103 ** 2])
print(dp[N])
sum = 0
sum += 105 ** 2
sum += 15 ** 2
sum += 8 ** 2
sum += 5 ** 2
print(sum)
