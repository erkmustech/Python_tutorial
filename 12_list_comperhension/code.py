number = [1,2,3]
double = []

for num in number:
    double.append(num*2)
print(double)


print("------simple way------")

double = [x*2 for x in number]
print(double)