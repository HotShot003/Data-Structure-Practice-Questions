# Sum of number Using Recursion 

def sum(n):
    
    if n == 0:
        return 0
    return n + sum(n-1)


n = int(input("Enter the number : "))
print(sum(n))