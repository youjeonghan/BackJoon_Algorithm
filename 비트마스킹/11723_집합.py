# 실버 5레벨    집합
from sys import stdin

li = set()
all = [i for i in range(1, 21)]

M = int(input())
for _ in range(M):
    command = list(stdin.readline().split())

    if command[0] == "add":
        li.add(int(command[1]))

    elif command[0] == "remove":
        try:
            li.remove(int(command[1]))
        except KeyError:
            pass

    elif command[0] == "check":
        if int(command[1]) in li:
            print(1)

        else:
            print(0)

    elif command[0] == "toggle":
        if int(command[1]) in li:
            li.remove(int(command[1]))

        else:
            li.add(int(command[1]))

    elif command[0] == "all":
        li = set(all)

    elif command[0] == "empty":
        li = set()