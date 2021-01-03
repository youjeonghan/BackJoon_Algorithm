# 1259_팰린드롬수

while 1:
    string = input()
    str_list = list(string)

    if string == "0":
        break

    if len(str_list) == 1:
        print("yes")

    for i in range(0, len(str_list) // 2):
        if str_list[i] != str_list[len(str_list) - 1 - i]:
            print("no")
            break

        if i == len(str_list) // 2 - 1:
            print("yes")
