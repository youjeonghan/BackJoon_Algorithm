# 실버 4레벨    숫자 카드 2
from collections import Counter
from sys import stdin

N = int(input())
card = list(map(int, stdin.readline().split()))
card = Counter(card)

M = int(input())
target = list(map(int, stdin.readline().split()))

for i in target:
    print(card[i], end=" ")
