# 실버 4레벨    나는야 포켓몬 마스터 이다솜
from sys import stdin

dic = {}
li = [0]

N, M = map(int, stdin.readline().split())

for i in range(1, N + 1):
    name = stdin.readline().rsplit()[0]
    dic[name] = i
    li.append(name)


for _ in range(M):
    command = stdin.readline().rsplit()[0]
    if command.isdigit():
        print(li[int(command)])

    else:
        print(dic[command])