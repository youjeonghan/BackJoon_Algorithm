# 실버 1레벨    이진 검색 트리
# 다시
# 틀렸음 (시간초과)
from sys import stdin
from pprint import pprint


def make_node(n):
    return {
        "node": n,
        "left": None,
        "right": None,
    }


def postorder(root):
    if root["left"]:
        postorder(root["left"])

    if root["right"]:
        postorder(root["right"])

    print(root["node"])


read = stdin.readline


root = make_node(0)
while 1:
    try:
        n = int(read())
    except:
        break

    if root["node"] != 0:
        temp = root
        while temp:
            if temp["node"] > n:
                if temp["left"] == None:
                    temp["left"] = make_node(n)
                    break
                else:
                    temp = temp["left"]
            else:
                if temp["right"] == None:
                    temp["right"] = make_node(n)
                    break
                else:
                    temp = temp["right"]

    else:
        root = make_node(n)

postorder(root)