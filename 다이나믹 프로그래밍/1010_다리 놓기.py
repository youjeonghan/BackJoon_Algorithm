# 실버 5레벨
# 다른 방법으로 풀기 (dp)

from math import factorial

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    n, m = min(n, m), max(n, m)
    print(factorial(m) // (factorial(m - n) * factorial(n)))
