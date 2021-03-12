# 골드 5레벨        평범한 배낭

from sys import stdin

read = stdin.readline
N, K = map(int, read().split())
li = []
for _ in range(N):
    li.append(list(map(int, read().split())))

bag = [[0] * (K + 1) for i in range(N + 1)]

for idx, (w, v) in enumerate(li):
    for weight in range(1, K + 1):
        if w <= weight:  # 자신을 포함 안했을때 최대값, 자신의가치 + 자신을 포함 안하고 자신의 무게만큼 빼고 최댓값
            bag[idx + 1][weight] = max(bag[idx][weight], bag[idx][weight - w] + v)
        else:
            bag[idx + 1][weight] = bag[idx][weight]

print(bag[N][K])