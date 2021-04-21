# 실버 3레벨    파도반 수열
N = int(input())
li = [0, 1, 1, 1, 2, 2, 3]
for i in range(94):
    li.append(li[(7 + i) - 1] + li[(7 + i) - 5])

for _ in range(N):
    M = int(input())
    print(li[M])