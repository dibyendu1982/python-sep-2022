
#~$ built-in data structures in python 

#! list - modification (insert, remove)
l = [11, 23, 36]
l.extend([1,3])
print(type(l), l)

#% set (unique)
s = {1, 2, 3}
s1 = {2,3,4,5}
print(s1.union(s))
print(type(s), s)

#? dictionary key:value pairs, unique keys 
d = {"id":1, "name":"Guido"}
print(type(d), d)

#* tuple - readonly quick record, tuple requires a comma to be considered as a tuple 
#* otherwise with single it will be considered as the type of the element, read only quick record
t = (1,2,3,4)
print(type(t), t)
t1 = (1)
print ("Not a tuple", type(t1), t1) #! Not a tuple instead prints a int
t2= (1,)
print("It is a tuple ",type(t2), t2)

# t3 = ("id": 1, "name": "Dibyendu", "account": 1232131, "balance":9000.00)