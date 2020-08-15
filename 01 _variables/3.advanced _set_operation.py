friends={"tarim","max","min","john"}
print(friends)
abrod_friends={"max", "john"}
print(abrod_friends)

#difference
local_friends=friends.difference(abrod_friends)  
print(f"local friends are{local_friends}")
print(abrod_friends.difference(friends))  #empty set 


#union
local_friends={"jamal", "hesen"}
foreign_friedns={"john","mony"}
total_friends=local_friends.union(foreign_friedns)   
print(total_friends)

#intercestion

art={"max","min","jon"}
sience={"max","jon"}
both=art.intersection(sience)
print(f"{both} are registed art and sience simultanously")