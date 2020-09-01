# 2839_설탕 배달
# 그리디
# 코드가 너무 비효율적으로 느껴져서 나중에 다른 코드를 참고해볼 예정이다

n = int(input())
cnt = 0
five_num = n // 5

for i in range(five_num, 0, -1):
    if (n - (5*i))%3 == 0 :
        cnt = cnt + i
        n = n - (5*i)
        break

if n % 3 == 0:
    cnt = cnt + n // 3
    print(cnt)

else:
    print(-1)
