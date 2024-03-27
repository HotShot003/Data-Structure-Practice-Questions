def simplepattern10(n):
    for i in range(2*n+1):
        for j in range(n+1):
            if i <n+1:
                if (i-j)>=0 and i<=(2*n+1)//2:
                    print(j+1,end=' ')
                else :
                    print(end=' ')
                    
            else :
                if i+j<=2*n:
                    print(j+1,end=' ')
                else :
                    print(end='  ')            
                    
        print()
        
simplepattern10(4)    

# 1     
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1                
             