class Person:    
    def bye (self):
        print("Bye ")   

class Person: 
    def hello(self):
        print("Hello")

p1 = Person()

# ? Monkey Patching bye to see if it can be called on p1 

def bye():
    print("monkey patching bye")

p1.bye = bye # ! Object Monkey patching 

p1.bye()

p1.hello()

# ? Monkey Patching the class 

def hi(self, name):
    print("hi from Monkey patched method", name)

Person.hi = hi  # TBD Class Monkey Patching setattr(ClassName, "Method_name", method_definition)


p2 = Person()

p2.hi("Dibyendu")
p2.bye()



