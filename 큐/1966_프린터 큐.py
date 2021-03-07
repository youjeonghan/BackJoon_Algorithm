# 실버 3레벨        프린터 큐
from sys import stdin
from collections import deque

T = int(stdin.readline())

for _ in range(T):
    N, M = map(int, stdin.readline().split())
    li = list(map(int, stdin.readline().split()))
    que = deque()
    for i in range(N):
        que.append((i, li[i]))

    li.sort()
    cnt = 0
    while cnt < 101:

        if que[0][1] == li[-1]:
            cnt += 1
            if que[0][0] == M:
                print(cnt)
                break

            li.pop()
            que.popleft()

        else:
            que.append(que.popleft())
