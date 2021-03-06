# 실버 4레벨        통계학
from sys import stdin
from collections import Counter

N = int(input())

li = []
for _ in range(N):
    li.append(int(stdin.readline()))
li.sort()
c = Counter(li)
c = list(c.items())
c.sort(key=lambda x: (-x[1], x[0]))

result = []
result.append(round(sum(li) / len(li)))
result.append(li[len(li) // 2])
if len(c) == 1 or (len(c) != 1 and c[0][1] != c[1][1]):
    result.append(c[0][0])
else:
    result.append(c[1][0])
result.append(abs(li[-1] - li[0]))

for i in result:
    print(i)