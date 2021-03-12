# 골드 5레벨        N-Queen
from collections import defaultdict

N = int(input())

cnt = 0
cen = defaultdict(int)
l = defaultdict(int)
r = defaultdict(int)


def re(idx):
    global cnt
    if idx == N:
        cnt += 1
        return

    for i in range(N):
        if not cen[i] and not l[i + idx] and not r[i - idx]:
            cen[i] = 1
            l[i + idx] = 1
            r[i - idx] = 1
            re(idx + 1)
            cen[i] = 0
            l[i + idx] = 0
            r[i - idx] = 0
    return


re(0)
print(cnt)