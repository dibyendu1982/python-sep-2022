
def natural():
    for value in range(1,11):
        print(value)
        
print(natural())

def gen_natural():
    yield 11
    yield 23
    yield 36 

iter = gen_natural()
print(next(iter))
print(next(iter))
print(next(iter))

for value in gen_natural():
    print(value)
