def add(x,y):
    print( x+y)
add(5,8)  
# the function was called
result=add(5,8)
# the function was called in a same way
print(result) 
# no fucntion was called and result is none, funtion retun none , that is what thdy do by default.

print("---next 2----")

def add(x,y):
    return x+y
add(5,8)
result=add(5,8)
print(result) 

# 13 , return only give result for print. 

print("---next 3----")

def mult(x,y):
    print(x*y)
    return x*y 

result=mult(5,8) 
print(result)  
# 40  print the result and show it in order result
# 40  the rutrun functin return the result for print. 




