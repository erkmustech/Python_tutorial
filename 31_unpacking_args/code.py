def mult(*args):

    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total


print(mult(1, 3, 5))
print(mult(8, 9, 23, 38))

print("---nex---")


def add(x, y):
    return x + y

nums = {"x": 15, "Y": 25}

