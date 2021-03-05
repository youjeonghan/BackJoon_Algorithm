# 브론즈 2레벨      분해합
def check(t):
    result = int(t)
    for i in t:
        result += int(i)

    return result


N = input()
len_N = len(N)
N = int(N)

min_N = N - (len_N * 9)
if min_N < 0:
    min_N = 0

result = 0
for i in range(min_N, N + 1):
    if N == check(str(i)):
        result = i
        break

print(result)