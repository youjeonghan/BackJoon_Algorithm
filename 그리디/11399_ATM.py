# 11399_ATM
# 그리디 알고리즘

n = int(input())
time_list = list(map(int, input().split()))
time_list.sort()
sum=0
wait=0
for i in range(0, n):
    sum = sum + (wait + time_list[i])
    wait = wait + time_list[i]

print(sum)