# 실버 2레벨    좌표 압축
from sys import stdin

N = int(stdin.readline().strip())

li = list(map(int, stdin.readline().strip().split()))
set = list(set(li))
set.sort()

dic = {}
for i in range(len(set)):
    dic[set[i]] = i

for i in li:
    print(dic[i], end=" ")
