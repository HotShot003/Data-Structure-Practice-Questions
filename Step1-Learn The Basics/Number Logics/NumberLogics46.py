# Write a Program to Find out all Pronic numbers present within a given
# range.

def range_PronicNumber(s,e):
    
    pricnum=[]
    
    for num in range(s,e+1):   
        i=1
        while i<=num//2:
            if i*(i+1)==num:
                pricnum.append(num)
            i+=1
    return pricnum        

print(range_PronicNumber(1,100))
