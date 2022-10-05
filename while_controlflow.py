def is_prime(value):
    max = 100000
    div = 2 
    while div < value:
        if value % div == 0:
            break
        div = div + 1
    else:
        return True
    return False

print(is_prime(36))

# Sum of the alternate even numbers 

max = 10

def sum_even_numbers(value):
    i = 0
    sum = 0
    while i < value:
        i += 1
        if i % 2 == 1: 
            continue 
        sum += i
    else:
        print ("sum", sum)

print(sum_even_numbers(800))
        
    
    