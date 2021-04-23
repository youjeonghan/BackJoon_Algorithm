# 골드 2레벨    합이 0인 네 정수

from sys import stdin
from collections import defaultdict

read = stdin.readline
n = int(read())
A, B, C, D = [], [], [], []

dic1 = {}
dic2 = {}
for _ in range(n):
    a, b, c, d = map(int, read().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

result = 0
for a in A:
    for b in B:
        dic1[a + b] = dic1.get(a + b, 0) + 1

for c in C:
    for d in D:
        result += dic1.get(-(c + d), 0)
print(result)