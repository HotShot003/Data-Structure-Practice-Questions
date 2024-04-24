# Write a Program to check whether the number is a Pronic Number or Not.
# res = n*(n+1) if res is int then it is pronic

def is_PronicNumber(n):
    orgi = n
    
    res = n * (n+1)
    
    if res<0:
        return f"{orgi} is not a Pronic Number"
    
    return f"{orgi} is a Pronic Number"
    
print(is_PronicNumber(4))   