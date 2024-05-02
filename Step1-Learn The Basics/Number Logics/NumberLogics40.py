# Write a Program to Find out all Magic numbers present within a
# given range.


def sum_of_digits(number):
    digit_sum = 0

    while number > 0:
        digit_sum += number % 10
        number //= 10

    return digit_sum

def is_magic_number(s,e):
    mgcnum=[]
    for number in range(s,e+1):
        orgi=number
        while number > 9:
            number = sum_of_digits(number)

        if number == 1:
            mgcnum.append(orgi)
    return mgcnum
# Example usage:

print(is_magic_number(1,100))
