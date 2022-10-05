class Person:
    def __init__(self, id, name):
        self.id = id        #! Field
        self.name = name    #! Field
    
    def print(self):
        print("id:", self.id, "name:", self.name)
        
guido = Person(1, "Dibyendu")

guido.print()
print(type(guido))
print(guido.id)

# import dis 
# print(dis.dis(guido.print))
q = Person(2, "Diby")

# * Monkey patch a field in an object 
guido.age = 67

def print_person(self):
    print(self.id, self.name)

setattr(Person, "print_person", print_person)

q.print_person()