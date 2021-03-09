# 실버 2레벨        조합
from itertools import combinations
from sys import stdin
from math import factorial as fac

read = stdin.readline
n, m = map(int, read().split())

result = fac(n) // fac(n - m) // fac(m)
# result = math.factorial(n)
print(int(result))