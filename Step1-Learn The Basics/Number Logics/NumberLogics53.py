# Write a Program to Find nth Perfect Square Number.

def is_PerfectSquare(n):
    
    i=1
    
    while i*i <= n:
        if i*i == n :
            return True
        i+=1
    return False



def nth_PerfectSquare(n):
    
    count = 0 
    
    curr_num=1
    
    while count < n :
        
        
        if is_PerfectSquare(curr_num):
            count +=1
        
        if count == n :
            return curr_num
    
        curr_num +=1
    return curr_num - 1        

print(nth_PerfectSquare(1))