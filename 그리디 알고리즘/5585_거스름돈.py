# 5585_거스름돈
# 그리디 알고리즘

cnt = 0
money = 1000
n = int(input())
money = money - n

cnt = cnt + money // 500
money = money % 500

cnt = cnt + money // 100
money = money % 100

cnt = cnt + money // 50
money = money % 50

cnt = cnt + money // 10
money = money % 10

cnt = cnt + money // 5
money = money % 5

cnt = cnt + money // 1
money = money % 1

print(cnt)