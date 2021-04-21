# 실버 3레벨    팩토리얼 0의 개수

N = int(input())
num = 1

for i in range(1, N + 1):
    num *= i

cnt = 0
for i in reversed(str(num)):
    if i == "0":
        cnt += 1
    else:
        break

print(cnt)