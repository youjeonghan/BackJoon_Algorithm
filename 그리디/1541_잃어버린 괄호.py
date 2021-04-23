# 실버 3레벨    잃어버린 괄호
import re
from sys import stdin

read = stdin.readline

li = read().rstrip()
num = list(map(int, re.compile(r"[0-9]+").findall(li)))
sym = re.compile(r"\+|-").findall(li)
if len(num) != len(sym):
    sym.insert(0, "+")
    result = num[0]
else:
    result = -num[0]
minus = 0

for idx in range(1, len(num)):
    if sym[idx] == "-":
        minus += num[idx]

    elif minus and sym[idx] == "+":
        minus += num[idx]

    else:
        result += num[idx]

result -= minus
print(result)
