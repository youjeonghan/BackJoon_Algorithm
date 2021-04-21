# 실버 3레벨    패션왕 신해빈

from sys import stdin
from collections import defaultdict

read = stdin.readline
n = int(read())
for _ in range(n):
    m = int(read())
    dic = defaultdict(list)
    for _ in range(m):
        name, col = read().rstrip().split()
        dic[col].append(name)

    result = 1
    for i in dic.values():
        result *= len(i) + 1

    result -= 1
    print(result)