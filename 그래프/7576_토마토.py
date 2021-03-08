# 실버 1레벨    토마토
# 서브큐 사용말고 while문 시작시 len(que)값만큼만 돌리는걸로 해도 될듯
from sys import stdin
from collections import deque

M, N = map(int, stdin.readline().split())
gp = [list(map(int, stdin.readline().split())) for _ in range(N)]


def bfs():
    move = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
    ]
    zero_cnt = 0
    que = deque()
    subque = deque()
    day = 0
    for i in range(N):
        for j in range(M):
            if gp[i][j] == 1:
                que.append((i, j))
            elif gp[i][j] == 0:
                zero_cnt += 1

    while que or subque:
        if zero_cnt == 0:
            break

        day += 1
        if not que:
            que = subque
            subque = deque()

        while que:
            t = que.popleft()
            for i in move:
                if (
                    0 <= (t[0] + i[0]) < N
                    and 0 <= (t[1] + i[1]) < M
                    and gp[t[0] + i[0]][t[1] + i[1]] == 0
                ):
                    zero_cnt -= 1
                    gp[t[0] + i[0]][t[1] + i[1]] = 1
                    subque.append((t[0] + i[0], t[1] + i[1]))

    if zero_cnt == 0:
        print(day)
    else:
        print(-1)


bfs()