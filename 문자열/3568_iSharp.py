# 실버 4레벨
# 15분 소요

base, input_list = input().split(maxsplit=1)
for i in input_list.split(", "):
    stack = []
    name = ""
    for j in range(len(i)):
        if j == 0:
            pass
        if i[j] == "]":
            stack.append("[")
        elif i[j] == "[":
            stack.append("]")
        elif i[j] == "*" or i[j] == "&":
            stack.append(i[j])
        elif i[j].isalpha():
            name += i[j]

    print(base + "".join(stack[::-1]) + f" {name};")
