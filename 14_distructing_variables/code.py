x=3, 5
x , y=3, 5
# x,y=(3, 5)  // tuple 
x=[(3,5)]
print(x,y)

print("----next 1---")

student_attendance = {"rolf":98, "bob":80,"Erk":100}

print(list(student_attendance.items()))

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}%")

print("----next 2---")

for t in student_attendance.items():
    print(t)


print("----next 3---")

people = [("bob",42,"sportman"),("max",39,"artist"),("min",34,"meth")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")


print("----next 4---")

# people = [("bob","sportman"),("max",39,"artist"),("min",34,"meth")]
# for name, age, profession in people:
#     print(f"Name: {name}, Age: {age}, Profession: {profession}")

# ValueError: not enough values to unpack (expected 3, got 2)


print("----next 5---")

people = [("bob","sportman"),("max",39,"artist"),("min",34,"meth")]
# for name, age, profession in people:
#     print(f"Name: {name[0]}, Age: {age[1]}, Profession: {profession[2]}")

# ValueError: not enough values to unpack (expected 3, got 2)

print("----next 6---")

people = ("max", 42, "sport")
name, _, profession = people  #use _ (underscor) for make the calue empety
print(people)
print(name, profession)

print("----next 6---")

num = [1,2,3,4,5]
head,*tail = [1,2,3,4,5]
print(head,tail)

*head, tail = [1,2,3,4,5]
print(head,tail)

