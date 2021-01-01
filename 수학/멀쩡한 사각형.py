from math import gcd

w, h = map(int, input().split())

gcd1 = gcd(w, h)

print((w * h) - (w + h - gcd1))
