# 실버 3레벨    1, 2, 3 더하기
from sys import stdin


def dp(i):
    if li[i] != 0:
        return li[i]

    else:
        return dp(i - 3) + dp(i - 2) + dp(i - 1)


li = [0] * 13
li[1] = 1
li[2] = 2
li[3] = 4

T = int(input())
for _ in range(T):
    n = int(stdin.readline())
    print(dp(n))


"""
3   -0 o
    -1 o
    -2 x

"""