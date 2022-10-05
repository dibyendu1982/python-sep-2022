
def header(char='*', count = 40):     #* <-- 20 is passed here 
    def decorator(fn): #* <-- the decorated function is passed here
        def inner(*args, **kwargs): #! This is the method which will be returned to the decorator factory
            print(char * count, "Decorator") ## Parameters passed to the decorator can be used inside the inner function
            fn(*args, *kwargs) 
            print(char * count, "Decorator") 
        return inner   #! It must return a function, which will be called 
    return decorator ## Decorator factory is being returned here 

 
@header('*', 20) #> Decorators with parameters are called as Decorator factories. 
def report():
    print("report here ")
    
    
@header('-', 40) #! If the header is without arguments, then function is the argument
def list_people(*args, **kwargs):
   print("people list", args, kwargs)

report() #* 
list_people()