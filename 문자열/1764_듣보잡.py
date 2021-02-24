# 실버 4레벨    듣보잡
from sys import stdin

N, M = map(int, stdin.readline().split())

listen = {}
see = []
result = []
for _ in range(N):
    listen[stdin.readline().rsplit()[0]] = 1

for _ in range(M):
    check = stdin.readline().rsplit()[0]
    try:
        if listen[check] == 1:
            result.append(check)
    except KeyError:
        pass

result.sort()
print(len(result))
for i in result:
    print(i)
