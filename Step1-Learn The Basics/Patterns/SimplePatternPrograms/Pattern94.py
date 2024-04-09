# Sol 1: Brute Force

def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if i-j>=0:
                if i>=0 and j==0:
                    print(i+1,end=' ')
                elif i>=0 and j==1:
                    print(n+1+i,end=' ')    
                elif i>=0 and j==2:
                    print(2*n+i ,end=' ')    
                elif i>=0 and j==3:
                    print(2*n+i+j-1 ,end=' ')    
                else :
                    print(4*n-1,end=' ')
                        
            else :
                print(end='')    
        print()

pattern(4)      

# 1 
# 2 6
# 3 7 10
# 4 8 11 13
# 5 9 12 14 15          