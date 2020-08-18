# lambda functin is a type fucntion that doesn't have name and only used to  return the value, exclusively used to return velus by used input . never used to perform actions 

lambda x, y : x+y
# add lambda x, y : x+y  we can use name if it needs
print((lambda x, y : x+y) (5,7))


print("----next 2----")

# def double(x):
#     return x*2

# sequence = [1, 3, 5, 9] 
# doubled = [double * 2 for x in sequence]
# doubled = list[map (double, sequence)]

print("----next 3----")

def double(x):
    return x*2

sequence = [1, 3, 5, 9] 
doubled = [(lambda x: x * 2)(x) for x in sequence]
doubled = list(map (lambda x: x*2, sequence))
print(doubled)
