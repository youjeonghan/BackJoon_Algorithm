# 실버 4레벨        균형잡힌 세상
from sys import stdin


while 1:
    string = stdin.readline().rstrip()
    stack = []
    result = "yes"

    if string == ".":
        break

    for i in string:
        if i == "[" or i == "(":
            stack.append(i)
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                result = "no"
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                result = "no"

    if stack:
        result = "no"

    print(result)
