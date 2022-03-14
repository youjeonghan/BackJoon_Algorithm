# 브론즈 1레벨

a = list(map(int, str(input())))
b = list(map(int, str(input())))
n = [0] * 16

for i in range(8):
    n[i * 2], n[i * 2 + 1] = a[i], b[i]

for i in range(15, 1, -1):
    for j in range(i):
        n[j] = (n[j] + n[j + 1]) % 10
print(str(n[0]) + str(n[1]))
