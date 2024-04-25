# Write a Program to check whether the number is a Pronic Number or Not

def is_PronicNumber(num):
    
    i=1
    while i<=num:
        if i*(i+1)==num:
            return f"{num} is a Pronic Number"
        i+=1
    return f'{num} is not a Pronic Number'

print(is_PronicNumber(12))
