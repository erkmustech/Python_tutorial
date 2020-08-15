grades = [90,89,78,59,69,99.100]
total = 0
amount = len(grades)
print(amount)

for grade in grades:
    total+=grade
print(total / amount)  
# print(f"average score of this group is {(total / amount):.2f}")  

print("-----simple way for loop-----")
grades2 = [90,89,78,59,69,59.100]
total = sum(grades2)
amount=len(grades2)
print(total / amount)