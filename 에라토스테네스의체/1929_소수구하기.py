# 실버 2레벨        소수 구하기
from sys import stdin


def prime_check():
    for i in range(2, N + 1):
        if li[i] == 1:
            for j in range(i + i, N + 1, i):
                li[j] = 0

            if M <= i <= N:
                result.append(str(i))


M, N = map(int, stdin.readline().split())
li = [1] * (N + 1)
li[0] = li[1] = 0
result = []
prime_check()
print("\n".join(result))