from itertools import combinations as com


def main():
    list1 = [1, 2, 3, 4]
    a = list(com(list1, 2))
    print(a)

    # x = input()
    # a = b = 0
    # for i in x:
    #     if i == "(":
    #         a += 1

    #     else:
    #         b += 1

    # if a == b:
    #     print("YES")
    # else:
    #     print("NO")


if __name__ == "__main__":
    main()