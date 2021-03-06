# 브론즈 1레벨      달팽이는 올라가고 싶다
from sys import stdin

a, b, v = map(int, stdin.readline().split())
cnt = 1
v -= a
cnt += v // (a - b)
if v % (a - b):
    cnt += 1
print(cnt)