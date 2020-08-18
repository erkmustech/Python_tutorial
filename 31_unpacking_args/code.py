def mult(*args):

    print(args)
    total=1
    for arg in args:
        total=total * arg
    return total

print(mult(1,3,5)) 