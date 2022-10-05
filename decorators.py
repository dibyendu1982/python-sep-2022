
def header(fn):     #! It takes a function (to which it is applied )
    def inner():
        print('-' * 40, "Decorator")
        fn()
        print('-' * 40, "Decorator")
    return inner    #! It must return a function, which will be called 

def report():
    print("report here ")
    
#* | decorator 
#* 
@header #! IF the header is without argument then function is the argument 
def list_people():
    print("Guido")
    print("Ritchie")
    print("Thomson")
    
list_people() #% -->header(report) will return inner, which will get called 

# # This may be called as a aspect oriented programming 
# # Decorators are also called as meta function which are called before or after the function executes. 


