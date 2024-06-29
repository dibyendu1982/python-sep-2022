
def print_forward_backtracking(i, N): 
    '''
    print numbers in a back tracking fashion from N to 1 
    '''
    if i > N:
        return 
    print_forward_backtracking(i+1, N)
    print(i) ## printing after the recursion is called backtracking 

# print_forward_backtracking(1,5)    

def print_in_sequence_backtracking(i, N): 
    '''
    print numbers in a back tracking fashion from 1 to N 
    '''
    if i < 1:
        return 
    print_in_sequence_backtracking(i-1, N)
    print(i, end=" ") ## printing after the recursion is called backtracking 


# print_in_sequence_backtracking(5,5)


def print_sequence_recursion(N):
    
    #Your code here
    if N < 1:
        return 
    print_sequence_recursion(N-1)
    print(N, end = " ") 
    
# print_sequence_recursion(10)


# summation of numbers in parameterized way 

def sum_parameterized_summation(i:int, sum:int):
    if i< 1:
        print(sum)
        return 
    return sum_parameterized_summation(i-1, sum+i)


def sum_sequence_recursion(n:int) -> int :
    if n == 0: 
        return 0
    return n + sum_sequence_recursion(n-1)

# x = sum_sequence_recursion(10)
# print(x)

def calculate_factorial(n:int) -> int:
    if n ==1:
        return 1
    return n * calculate_factorial(n-1)

print(calculate_factorial(5))
    

# Reverse array using recursion 


def reverse_array_recursion(i, array: list):
    length = len(array)
    
    if i >= length/2:
        return 
    # swap_element(array[i], array[length-i-1], array)
    tmp = array[i]
    array[i] = array[length-i-1]
    array[length-i-1] = tmp
    
    reverse_array_recursion(i+1, array)
    return array
    

# array = [1,2,3,4,5] 
# print(reverse_array_recursion(0, array))

def check_palindrome(i ,test: str):
    array_character = list(test)
    size = len(array_character)
    ## If the comparison till the middle is successful then no need to go further 
    if i >= size/2:
        return True
    ## Be
    if array_character[i] != array_character[size-i-1]:
        return False
    
    return check_palindrome(i+1, test)

print(check_palindrome(0, "MADSAM"))


    
    
    
    
    
    
