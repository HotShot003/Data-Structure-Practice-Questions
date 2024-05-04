# Write a Program to Find out all Trimorphic numbers present within a given
# range.


def cube(n):
    return n * n * n


def range_TrimorphicNumber(s,e):
    
    trinum=[]
    
    for num in range(s,e+1):
        
        orgi = num 
        num = cube(num)
        if num%10 == orgi%10:
            trinum.append(orgi)
    
    return trinum



print(range_TrimorphicNumber(200,300))        