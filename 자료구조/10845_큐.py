# 10845_큐
# 자료구조
import sys

cnt = int(input())
queue = []

for i in range(0, cnt):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        queue.append(int(cmd[1]))

    elif cmd[0] == "pop":
        if len(queue) == 0:
            print(-1)
            continue
        print(queue.pop(0))

    elif cmd[0] == "size":
        print(len(queue))

    elif cmd[0] == "empty":
        if len(queue) == 0:
            print(1)

        else:
            print(0)

    elif cmd[0] == "front":
        if len(queue) == 0:
            print(-1)
            continue
        print(queue[0])

    elif cmd[0] == "back":
        if len(queue) == 0:
            print(-1)
            continue
        print(queue[len(queue)-1])

