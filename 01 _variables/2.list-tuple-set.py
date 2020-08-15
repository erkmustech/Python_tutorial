l=["max","bob","john"]   # this is list, orderted and can be manipulated 

t=("tom", "max", "relk","convention")   #tuple  doestn't allowed to modification
s={"jibrish","swagger", "ostantatius","swagger"} #set, unorderd , not dupliacted 

print(t)
# t.append("min")   you can't add value in tuple
# print(t)

l.append("min")
print(l)
l.remove("max")
print(l)


s.add("max")
s.add("max")
print(s)
# in set , it is unordered and not allowed to duplicate values 



