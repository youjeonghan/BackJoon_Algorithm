# 실버 5레벨
# 5분 소요

s = int(input())

i = 1
n = 0
cnt = 0
while n <= s:
    n += i
    i += 1
    cnt += 1

print(cnt - 1)
