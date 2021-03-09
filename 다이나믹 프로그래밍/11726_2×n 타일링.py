# 실버 3레벨    2×n 타일링
import sys

limit_number = 15000
sys.setrecursionlimit(limit_number)


def check(n):
    start = 3

    while start <= n:
        li[start] = li[start - 2] + li[start - 1]
        start += 1


n = int(input())

li = [0] * 1001
li[1] = 1
li[2] = 2
check(n)
print(li[n] % 10007)
