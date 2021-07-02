def make_node(n):
    return {
        "node": n,
        "left": None,
        "right": None,
    }


root = make_node(0)

while root:
    print(root)
    root = 0
