# 골드 4레벨        후위 표기식
# 다시
from sys import stdin
from collections import deque

open = close = 0

str = stdin.readline().rstrip()
str = deque(str)
result = ""


def check(root):
    result = ""
    stack = []
    while str:
        i = str.popleft()
        if i.isalpha() or i.isdigit():
            result += i
            if stack and (stack[-1] == "*" or stack[-1] == "/"):
                while stack and (stack[-1] == "*" or stack[-1] == "/"):
                    result += stack.pop()

        elif i == "(":
            result += check(0)

        elif root == 0 and i == ")":
            while stack:
                result += stack.pop()
            return result

        else:
            if (i == "+" or i == "-") and stack and (stack[-1] == "+" or stack[-1] == "-"):
                while stack:
                    result += stack.pop()
            stack.append(i)

    while stack:
        result += stack.pop()
    return result


print(check(root=1))