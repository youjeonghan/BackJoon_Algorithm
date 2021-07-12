# 골드 2레벨    합이 0인 네 정수

from sys import stdin
from collections import defaultdict

read = stdin.readline
n = int(read())
A, B, C, D = [], [], [], []

dic1 = defaultdict(int)
dic2 = defaultdict(int)
for _ in range(n):
    a, b, c, d = map(int, read().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)


# for a, c in zip(A, C):
#     for b, d in zip(B, D):
#         dic1[a + b] += 1
#         dic2[c + d] += 1

result = 0
for a in A:
    for b in B:
        dic1[a + b] += 1

for c in C:
    for d in D:
        result += dic1[-(c + d)]

print(result)