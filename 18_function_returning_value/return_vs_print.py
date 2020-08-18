print("-------1vs------")
def add(a,b):
    print(a+b)
add(4,5)

print("-------2vs------")

def add(a,b):
    return a+b
add(4,5)
print(add(4,5))

print("-------3vs------")

def add(a,b):
    return a+b
result=add(4,5)
print(result)


print("-------4vs------")

def add(a,b):
    return a+b
print(add(4,5))
add(4,5)

print("-------5vs------")

def add(a,b):
    print(a+b)
print(add(5,8))    

# 13
# None   

print("-------6vs------")

def add(a,b):
    return a+b   # function will stop here and back 
    print(a+b)

result=add(5,8)
print(result)    


