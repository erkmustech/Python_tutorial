magic_number = 7
userdata = input("please inter 'Y' if you would like to play!").lower()

if userdata == "y":
# if userdata in ("y", "Y"):
    userNum = int(input("please inter the megic num you can guess!"))
    if userNum == magic_number:
        print("you win")
    # elif magic_number -  userNum in (1,-1):
    elif abs(magic_number -  userNum) == 1:
        print("you were off by one")

    else:
        print("you are wrong")
    print("game is over!")
else:
    print("see you!")        