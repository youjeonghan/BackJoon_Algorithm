# 실버 3레벨    구간 합 구하기 4
from sys import stdin

read = stdin.readline

N, M = map(int, read().split())
li = list(map(int, read().split()))
total = [0] * (len(li) + 1)
for idx in range(len(li)):
    total[idx + 1] = total[idx] + li[idx]

for _ in range(M):
    s, e = map(int, read().split())
    print(total[e] - total[s - 1])
