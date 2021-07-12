# 실버 2레벨    쿼드트리

from collections import Counter
from sys import stdin


def check(sy, sx, size):
    cnt = [0, 0]
    num = size ** 2
    for y in range(sy, sy + size):
        for x in range(sx, sx + size):
            cnt[gp[y][x]] += 1
    if cnt[0] == num:
        result = 0
    elif cnt[1] == num:
        result = 1
    else:
        result = -1
    return result


def divide_conquer(sy, sx, size):
    check_result = check(sy, sx, size)
    if check_result == 0:
        return "0"
    elif check_result == 1:
        return "1"
    else:
        result = ""
        t = size // 2
        result += divide_conquer(sy, sx, t)
        result += divide_conquer(sy, sx + t, t)
        result += divide_conquer(sy + t, sx, t)
        result += divide_conquer(sy + t, sx + t, t)
        return "(" + result + ")"


read = stdin.readline
N = int(read())
gp = [list(map(int, read().strip())) for _ in range(0, N)]
print(divide_conquer(0, 0, N))
