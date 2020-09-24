# 백준 10799_쇠막대기
# 분류 자료 구조

li = []
li = input()
cnt=0
stick=0
for i in range(0, len(li)):

    if i == len(li)-1:
        cnt = cnt+1

    elif li[i] =="(" and li[i+1]==")":
        cnt = cnt + stick

    elif li[i-1] =="(" and li[i]==")":
        continue

    elif li[i] == "(":
        stick +=1

    elif li[i] == ")":
        stick -=1
        cnt +=1

print(cnt)