def simplepattern1(n):
    print("Simple Pattern 1")
    for i in range(n+1):
        for j in range(i+1):
            if i-j>=0:
                print('*',end=' ')
            else :
                print(end='')
        print()            
        
        
simplepattern1(4)        

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
