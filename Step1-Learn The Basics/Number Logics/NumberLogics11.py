# Write a Program to calculate prime Factors of number.Write a Program to calculate prime Factors of number.

def prime_factors(num):
    found_factor = False  # Flag to check if any factor was found
    for i in range(2, num):
        if num % i == 0:  # Check if i is a factor of num
            print(i,end=' ')
            num = num // i  # Update num by dividing with i
            found_factor = True
            break  # Break out of the loop after finding one factor
    
    if not found_factor:
        # If no factor was found in the loop, num is prime itself
        print(num,end=' ')

        # Optional: Stop recursion if num is prime (base case)
        return
    
    # Recursively find prime factors of the updated num
    prime_factors(num)

# Example usage
number = int(input("Enter a number: "))
print("Prime factors:",end=' ')
prime_factors(number)
