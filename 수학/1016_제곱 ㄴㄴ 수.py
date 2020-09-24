# 1016_제곱 ㄴㄴ 수

# 초기접근 답은 나오나 시간초과함
# import math
# min, max = map(int, input().split())
#
# cnt=0
# for i in range(min, max+1):
#     for j in range(2, i+2):
#         if pow(j,2) > i:
#             cnt +=1
#             break
#         if i%pow(j,2) == 0:
#             break
#
# print(cnt)

import math
min, max = map(int, input().split())
validate = [1 for i in range(max-min+1)]
cnt=0
i=2
while i**2 <= max:
    mul = min // i**2
    # if min// i**2 !=0:
    #     mul +=1
    while mul * (i**2) <= max:
        if mul * (i**2) - min >= 0 and mul * (i**2) - min <= max-min:
            validate[mul * (i**2) - min] = 0
        mul +=1
    i +=1

print(sum(validate))
