# Write a program to check whether a given number is Friendly pair or not.


def diviosr_Sum(n):
    sum = 1
    i=2
    while i <= n//2:
        if n % i == 0:
            sum += i
        i += 1
    return sum
# print(diviosr_Sum(6))    

def is_Friendly(num1,num2):
    if diviosr_Sum(num1) == num2 and diviosr_Sum(num2) == num1:
        return f"{num1} and {num2} form a Friendly Pair."
    
    return f"{num1} and {num2} do not form a Friendly Pair."



print(is_Friendly(220,284))
    
 

