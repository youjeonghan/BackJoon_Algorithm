# 실버 1레벨    케빈 베이컨의 6단계 법칙

from sys import stdin

read = stdin.readline
n, m = map(int, read().split())

gp = [[float("inf")] * (n + 1) for _ in range(n + 1)]
short = [[float("inf")] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, read().split())
    gp[s][e] = 1
    gp[e][s] = 1

for i in range(1, n + 1):
    gp[i][i] = 0


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            gp[i][j] = min(gp[i][j], gp[i][k] + gp[k][j])

min_v = [float("inf"), 0]
for i in range(1, n + 1):
    sum = 0
    for v in gp[i]:
        sum += v if v != float("inf") else 0

    if sum < min_v[0]:
        min_v = sum, i

print(min_v[1])