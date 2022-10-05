print("globals","-" * 80)

print(globals())

print("-" * 80)

def hello():
    locals()['x'] = 1 # same as x = 1 
    y = 1
    z = 1
    print("locals within method","-" * 80) 
    print(locals())
    print("global within method","-" * 80)
    print(globals())

print ("__name__ value", __name__)
a = 1
globals()['b'] = 2  #  same as saying a = 1 
print("globals","-" * 80) 
print(globals())
print("locals","-" * 80) 
print(locals())
hello()