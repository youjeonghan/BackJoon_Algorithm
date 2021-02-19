# 실버 5레벨    나이순 정렬
from sys import stdin

N = int(input())

li = []
for _ in range(N):
    age, name = map(str, stdin.readline().split())
    age = int(age)
    li.append((age, name))

li.sort(key=lambda x: x[0])

for i in li:
    print(i[0], i[1])