def pattern(n):
    for i in range(2*(n-1)+1):
        for j in range(n):
            if i<n:
                if i-j>=0:
                    print(chr(65+(n-j-1)),end=' ')
                else:print(end='')
            else :
                if i+j<2*(n-1)+1:
                    print(chr(65+(n-j-1)),end=' ')
                else: print(end='')
        print()                    
        
pattern(4)

# D    
# D C   
# D C B  
# D C B A 
# D C B  
# D C   
# D         
        