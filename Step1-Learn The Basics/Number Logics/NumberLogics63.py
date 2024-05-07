# Write a Program to Find nth Happy Number.


def sqr(n):
    return n ** 2

def is_happy_number(n):
    seen_numbers = set()  # Set to keep track of visited numbers
    current_number = n
    
    while current_number != 1 and current_number not in seen_numbers:
        seen_numbers.add(current_number)
        next_number = 0
        
        # Calculate the sum of squares of digits of the current number
        while current_number > 0:
            next_number += sqr(current_number % 10)
            current_number //= 10
        
        current_number = next_number  # Update current number
    
    return current_number == 1

def nth_HappyNumber(n):
    
    count = 0 
    curr_num = 1
    
    while count <= n :
        
        if is_happy_number(curr_num):
            count += 1

        if count == n:
            return curr_num

        curr_num += 1
    return curr_num - 1

print(nth_HappyNumber(2))   