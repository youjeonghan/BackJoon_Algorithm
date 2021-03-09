# 실버 1레벨        트리 순회
from collections import defaultdict
from sys import stdin

read = stdin.readline
N = int(read())
tree = defaultdict(list)
for _ in range(N):
    root, l, r = read().strip().split()
    tree[root] = [l, r]
result = ["", "", ""]


def traverse(node):
    result[0] += node
    if tree[node][0] != ".":
        traverse(tree[node][0])

    result[1] += node
    if tree[node][1] != ".":
        traverse(tree[node][1])

    result[2] += node


traverse("A")

for i in result:
    print(i)