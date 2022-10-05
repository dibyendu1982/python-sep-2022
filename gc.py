import sys

#! MAnual Memory Management  

class Person: 
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        
    def __del__(self):
        print("Person reference deleted with the id: ", self.id)
n1 = Person(2, "Shweta")        

p1 = Person(1, "Dibyendu")
p2 = p1
p3 = p1 

n2 = n1 
n3 = n2
print("p1", sys.getrefcount(p1))
print("p2", sys.getrefcount(p2))

print("n1", sys.getrefcount(n1))
print("n2", sys.getrefcount(n2))
print("n3", sys.getrefcount(n3))


# # At this point the generational GC will kick in 