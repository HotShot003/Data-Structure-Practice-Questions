# Write a Program to Find out all Sunny numbers present within a given
# range.



def perfectSq(n):
    i=1
    while i*i <= n:
        if i*i == n:
            return True
        i += 1
    return False    

# print(perfectSq(25))   
  

def range_SunnyNum(s,e):
    
    sunnum=[]
    
    for n in range(s,e+1):
        
        orgi  = n
        
        if perfectSq(n+1) == True:
            sunnum.append(orgi)
            
    return sunnum

print(range_SunnyNum(1,100))
        
         