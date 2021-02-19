# 실버 4레벨    덱
from collections import deque
from sys import stdin

dec = deque()
N = int(input())
for i in range(N):

    command = list(stdin.readline().split())

    if command[0] == "push_front":
        dec.appendleft(int(command[1]))

    elif command[0] == "push_back":
        dec.append(int(command[1]))

    elif command[0] == "pop_front":
        if dec:
            print(dec.popleft())
        else:
            print(-1)

    elif command[0] == "pop_back":
        if dec:
            print(dec.pop())
        else:
            print(-1)

    elif command[0] == "size":
        print(len(dec))

    elif command[0] == "empty":
        if dec:
            print(0)
        else:
            print(1)

    elif command[0] == "front":
        if dec:
            print(dec[0])
        else:
            print(-1)

    elif command[0] == "back":
        if dec:
            print(dec[-1])
        else:
            print(-1)