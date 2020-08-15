student_attendance = {"rolf":98, "bob":80,"Erk":100}

for student in student_attendance:
    print(student) 

print("---next 1 ----")   

student_attendance = {"rolf":98, "bob":80,"Erk":100}

for student in student_attendance:
    print(f"{student}:{student_attendance[student]}%") 

print("---next 2----")   

for student,attendance in student_attendance.items():
    print(f"{student}: {attendance}%")


print("---next 3----")   

if "bob" in student_attendance:
    print(f"Bob: {student_attendance['bob']}")

else:
    print("Bob is not a student")    


print("---next 4----")   

student_attendance = {"rolf":96, "bob":80,"Erk":100}
attendance_values = student_attendance.values();
print(sum(attendance_values) / len(attendance_values))
