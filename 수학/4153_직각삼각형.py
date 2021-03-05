# 브론즈 3레벨      직각삼각형
from sys import stdin

while True:
    com = list(map(int, stdin.readline().strip().split()))
    com.sort()
    if com[0] == com[1] == com[2] == 0:
        break

    elif com[2] ** 2 == com[1] ** 2 + com[0] ** 2:
        print("right")

    else:
        print("wrong")