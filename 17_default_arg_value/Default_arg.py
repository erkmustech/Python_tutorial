def add(x,y=8):
    print(x+y)

add(5)    
#y was given value , when we called the fun the x takes only velua as we already decrelared y. 

default_a = 5

def mul(b, a = default_a):
    result= b * a
    print(result)

mul(6)

default_a = 9  
# we can't change the default_a value as it is created as the funtion wad built.

mul(6)
