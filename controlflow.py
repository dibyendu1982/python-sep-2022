# ! Greatest Super hero program 

# ? Control Flow Demo using if 
spiderman = 30
batman = 10 
superman = 40

if batman > spiderman:
    if batman > superman:
        print("batman is greatest")
    else:
        if superman > spiderman:
            print("superman is greatest")
else:
    if spiderman > superman: 
        print("spiderman is greatest")
    else:
        print("Superman is greatest")

sumOfNatural = 0

# ? Control flow in For 

for i in range(1, 21):
    sumOfNatural = sumOfNatural + i
    
print(sumOfNatural)


# ? Control Flow using while 

max = 10000
sum = 0 
while max > 0:
    sum += max
    max -= 1
print(sum)