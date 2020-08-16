print("---1. fanctin with two param----")
def add(x, y):
    result=x+y
    print(result)

add(4, 9)

print("--- 2.fanctin with no param----")

def hello():
    print("hello")

# hello("bob")
# TypeError: hello() takes 0 positional arguments but 1 was given

print("--- 3.fanctin with with arg----")

def hello(name):
    print(f"hello, {name}")

hello("bob")

