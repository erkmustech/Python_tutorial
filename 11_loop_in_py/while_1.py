# there are 2 types loop in python
# 1. repeat the code in amount of time based on the condition 
# 2. reapeat the code as long as the condition is ture


magic_number = 7
userdata = input("would you like to play? (Y/n)")

while userdata !="n":
    userNum = int(input("please inter the megic num you can guess!"))
    if userNum == magic_number:
        print("you win")
    elif magic_number -  userNum in (1,-1):
        print("you were off by one")
    else:
        print("you are wrong")
    print("game is over!")
else:
    print("see you!")  

userdata = input("would you like to play? (Y/n)")          