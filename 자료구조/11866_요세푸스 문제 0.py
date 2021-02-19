# 실버 4레벨    요세푸스 문제 0

N, K = map(int, input().split())
li = [i for i in range(1, N + 1)]
result = []
idx = 0
for i in range(1, N + 1):
    idx += K
    if idx > len(li):
        idx %= len(li)
        if idx == 0:
            idx = len(li)

    result.append(li.pop(idx - 1))
    if idx == 1:
        idx = len(li)
    else:
        idx -= 1

answer = "<"
for i in range(len(result)):
    if i + 1 == len(result):
        answer += f"{result[i]}>"
    else:
        answer += f"{result[i]}, "

print(answer)