# Write a Program to check whether the number is Magic Number
def sum_of_digits(number):
    digit_sum = 0

    while number > 0:
        digit_sum += number % 10
        number //= 10

    return digit_sum

def is_magic_number(number):
    while number > 9:
        number = sum_of_digits(number)

    return number == 1

# Example usage:
num = 55
if is_magic_number(num):
    print(f"{num} is a Magic Number.")
else:
    print(f"{num} is not a Magic Number.")
