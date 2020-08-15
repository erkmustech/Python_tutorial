friends = ["max", "min", "john" ,"erk"]
starts_m = []

for friend in friends:
    if friend.startswith("m"):
        starts_m.append(friend)

print(starts_m)        

print("-----simple way------")

friends = ["max", "min", "john" ,"erk"]
# starts_m = [friend for friend in friends if friend.startswith("m")]
# print(starts_m)

# print(friends)
# print(starts_m)
# print(friends is starts_m)
print("friends: ",id(friends),"starts_m:", id(starts_m))
