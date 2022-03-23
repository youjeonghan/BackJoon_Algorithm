# 골드 4레벨

from itertools import combinations
import sys

read = sys.stdin.readline
answer = 0


def tracking(idx):
    if len(sign) == k:
        check(sign)
        return
    if idx >= len(union):
        return

    sign.append(union[idx])
    idx += 1
    tracking(idx)
    sign.pop()
    tracking(idx)


def check(sign):
    global answer
    temp = set(sign)
    cnt = 0
    for i in arr:
        if len(i - temp) == 0:
            cnt += 1
    answer = max(answer, cnt)


n, k = map(int, read().split())
arr = []
union = set()
for _ in range(n):
    arr.append(set(read().strip()))
    union = union | arr[-1]
if k < 5:
    print(0)
    sys.exit(0)
elif k >= len(union):
    print(n)
    sys.exit(0)

union -= set(["a", "n", "t", "i", "c"])
union = list(union)
sign = ["a", "n", "t", "i", "c"]

tracking(0)
print(answer)