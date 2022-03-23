# 실버 2레벨
# 55분 소요
# eval로 풀어서 다시 풀어보기

sign = list(input())

answer_str = "("
stack = [sign[0]]
dic = {
    ")": "2",
    "]": "3",
}

for idx in range(1, len(sign)):
    t = sign[idx]
    if t == "(" or t == "[":
        stack.append(t)
        answer_str += "+("
    elif (t == ")" and sign[idx - 1] == "(") or (t == "]" and sign[idx - 1] == "["):
        answer_str += dic[t] + ")"
        stack.pop()
    elif stack and ((t == ")" and stack[-1] == "(") or (t == "]" and stack[-1] == "[")):
        answer_str += ")*" + dic[t] + ""
        stack.pop()
    else:
        stack.append(t)


if stack:
    print(0)
else:
    print(eval(answer_str))