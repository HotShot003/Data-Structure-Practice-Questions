# Write a program to find out all primes numbers present within a
# given range.


def is_Primes(n):
      
    if (n!=2 and n%2==0) or (n!=3 and n%3==0) or (n!=5 and n%5==0) or n==1:
        return False
    
    i=5
    while i*i<n:
        
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    
    return True

# print(is_Primes(1))    
def range_Prime(s,e):
    prime=[]
    for n in range(s,e+1):
        if is_Primes(n):
            prime.append(n)
    return prime

print(range_Prime(1,100))
        
        