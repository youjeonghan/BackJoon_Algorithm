# 실버 5레벨        수 정렬하기 3
from sys import stdin, stdout

N = int(stdin.readline())
dic = {}
for _ in range(N):
    x = int(stdin.readline())
    if dic.get(x) == None:
        dic[x] = 1
    else:
        dic[x] += 1


for i in range(1, 10001):
    if dic.get(i):
        for _ in range(dic.get(i)):
            stdout.write(f"{i}\n")