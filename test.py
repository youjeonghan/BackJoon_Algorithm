def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        return a // b


def dfs(depth):
    if depth == n - 1:
        if not _min:
            _min.append(numbers[n - 1])
            _max.append(numbers[n - 1])
        else:
            _min = min(_min[0], numbers[n - 1])
            _max = max(_max[0], numbers[n - 1])
        return

    for i in range(4):
        if operations[i] != 0:
            operations[i] -= 1
            origin = numbers[i + 1]
            numbers[i + 1] = calculate(numbers[i], opIdx[i], numbers[i + 1])
            dfs(depth + 1)
            operations[i] += 1
            numbers[i + 1] = origin


n = int(input())
numbers = list(map(int, input().split()))
operations = list(map(int, input().split()))
opIdx = ["+", "-", "*", "/"]
_min = ["asd"]
_max = ["aa"]

dfs(0)
print(_min, _max)

# 2
# 5 6
# 0 0 1 0