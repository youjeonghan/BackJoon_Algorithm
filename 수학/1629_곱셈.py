# 실버 1레벨        곱셈
from sys import stdin

read = stdin.readline
A, B, C = map(int, read().split())
result = 0


def mul(x, y):
    if y == 1:
        return x
    else:
        temp = mul(x, y // 2)
        if y % 2 == 0:
            return temp ** 2 % C
        else:
            return temp ** 2 * x % C


print(mul(A, B) % C)
