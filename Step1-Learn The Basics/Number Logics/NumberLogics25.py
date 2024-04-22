# Write a Program to check whether the number is Happy Number or Not


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

# Prompt the user for input and check if the number is a Happy number
user_input = input("Enter a number: ")

try:
    number = int(user_input)
    if is_happy_number(number):
        print(f"{number} is a Happy number")
    else:
        print(f"{number} is not a Happy number")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
