# 실버 2레벨        트리의 부모 찾기
from collections import defaultdict, deque
from sys import stdin

read = stdin.readline

N = int(read())

visit = [0] * (N + 1)
dic = defaultdict(set)
for _ in range(N - 1):
    a, b = map(int, read().split())
    dic[a].add(b)
    dic[b].add(a)


def bfs():
    que = deque()
    que.append(1)
    visit[1] = 1
    while que:
        t = que.popleft()
        for i in dic[t]:
            if visit[i] == 0:
                que.append(i)
                visit[i] = t


bfs()
for i in range(2, N + 1):
    print(visit[i])
