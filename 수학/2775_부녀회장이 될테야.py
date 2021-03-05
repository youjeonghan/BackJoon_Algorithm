# 브론즈 2레벨      부녀회장이 될테야
from sys import stdin


def check(k, n):
    if apt[k][n - 1] != 0:
        return apt[k][n - 1]

    else:
        apt[k][n - 1] = check(k, n - 1) + check(k - 1, n)
        return apt[k][n - 1]


T = int(input())
apt = [[1 if i == 0 else 0 for i in range(14)] for i in range(100)]
apt[0] = [i for i in range(1, 15)]
for _ in range(T):
    k = int(stdin.readline())
    n = int(stdin.readline())
    print(check(k, n))
