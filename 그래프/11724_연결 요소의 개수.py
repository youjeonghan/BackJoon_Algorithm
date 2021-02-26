# 실버 2레벨    연결 요소의 개수
# bfs 이용
from collections import deque
from sys import stdin


def bfs():
    cnt = 0
    deq = deque()

    for i in range(1, N + 1):
        if visit[i] == 0:
            visit[i] = 1
            deq.append(i)

            while deq:
                t = deq.popleft()
                for j in gp[t]:
                    if visit[j] == 0:
                        visit[j] = 1
                        deq.append(j)
            cnt += 1

    return cnt


cnt = 0

N, M = map(int, stdin.readline().strip().split())
gp = [[] for _ in range(N + 1)]
visit = [0] * (N + 1)


for i in range(M):
    a, b = map(int, stdin.readline().strip().split())
    gp[a].append(b)
    gp[b].append(a)

print(bfs())