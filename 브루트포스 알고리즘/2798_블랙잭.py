# 브론즈 2레벨      블랙잭
import sys
from itertools import combinations

result = 0
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
gap = sys.maxsize

com = list(combinations(li, 3))

com = [sum(i) for i in com]

for i in com:
    if gap > m - i and m >= i:
        gap = m - i
        result = i

print(result)
