# in pythong veribale , 1. dont' use same name, 2. careful with the paramers inside brackts.'

# def print():
#     print("hello")

# print()   

# print("----rul no 3---- don't reuse the callable veribale name ")

# friends = ["bob","max"]

# def add_friend():
#     friend_name = input ("enter you friend name!")
#     # friends = friends + [friend_name]
#     f = friends + [friend_name]

# add_friend()

print("---problem 3----")
#don't call the varibale befor it's defination
# say_hello()
# def say_hello():
#     print("hello")

friends=[]
def add_friend():
    friends.append("bob")
    print("welcome bob")
add_friend()   
add_friend()   
add_friend()   
add_friend()  

print(friends)

#NameError: name 'say_hello' is not defined


print("---problem 4----")
#don't call the varibale befor it's defination



