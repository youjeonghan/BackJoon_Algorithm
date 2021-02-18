# 실버 5레벨    최대공약수와 최소공배수

from math import gcd

a, b = map(int, input().split())
gcd_num = gcd(a, b)
print(gcd_num)
print(int(gcd_num * a * b / gcd_num ** 2))
