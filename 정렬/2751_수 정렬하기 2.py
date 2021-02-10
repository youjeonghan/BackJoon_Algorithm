# 실버5     2751_수 정렬하기 2
import sys

n = int(input())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

li.sort()
for i in li:
    print(i)