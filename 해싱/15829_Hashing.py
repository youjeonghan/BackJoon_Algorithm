# 브론즈 2레벨      Hashing

result = 0
r = 31
M = 1234567891

L = int(input())
s = input()
for idx, i in enumerate(s):
    result += (r ** idx) * (ord(i) - ord("a") + 1)

print(result % M)
