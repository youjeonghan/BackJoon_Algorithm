# 실버 3레벨        N과 M (5)
from itertools import permutations
from sys import stdin

read = stdin.readline

N, M = map(int, read().split())
li = list(map(int, read().split()))
li.sort()
result = list(permutations(li, M))

for i in result:
    for j in i:
        print(j, end=" ")

    print()