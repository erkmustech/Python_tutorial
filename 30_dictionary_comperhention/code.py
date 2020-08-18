users = [
    (0,"max", "maxmax"),
    (1,"min", "minmin"),
    (2,"bob", "1111"),
    (3, "username", "12321")
]

username_mapping = {user[1]: user for user in users}
username_input = input("inter your username!")
password_input = input("inter your password!")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("your detailes are corract!")
else:
    print("your details are incorract!")    

print("----next----")

users = [
    (0,"max", "maxmax"),
    (1,"min", "minmin"),
    (2,"bob", "1111"),
    (3, "username", "12321")
]

username_mapping = {user[1]: user for user in users}
print(username_mapping)
