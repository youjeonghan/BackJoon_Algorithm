# 실버 3레벨        N과 M (2)
from itertools import combinations
from sys import stdin

read = stdin.readline

N, M = map(int, read().split())
li = [i + 1 for i in range(N)]
result = list(combinations(li, M))
for i in result:
    for j in i:
        print(j, end=" ")
