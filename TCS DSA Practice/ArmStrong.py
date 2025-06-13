def is_armstrong(n):
    orgi = n
    temp=n
    l_digi=0
    sum_digi=0
    while temp > 0:
        temp //= 10
        l_digi +=1
    
    temp = n
    
    while temp > 0 :
        digi = temp % 10
        sum_digi += digi ** l_digi
        temp//=10
    return sum_digi == orgi         

# Input handling
n = int(input("Enter a number: "))
print(is_armstrong(n))