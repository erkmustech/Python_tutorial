magic_number = 7

while True:
    userdata = input("would you like to play? (Y/n)")

    if userdata == "n":
        print("game is over!")
        break

    userNum = int(input("please inter the megic num you can guess!"))
    if userNum == magic_number:
        print("you win")
    elif magic_number -  userNum in (1,-1):
        print("you were off by one")
    else:
        print("you are wrong")

