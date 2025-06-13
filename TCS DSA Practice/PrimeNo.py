# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     # Check odd divisors up to sqrt(n)
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

def is_prime(i):
    
    if i % 2 != 0 or i % 3 !=0 or i % 5 != 0 :
            return True
    else: 
        return False 
        
        

# Input handling
n = int(input())
print(is_prime(n))