# Pascals Triangle :

# Type 1 :
# Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.

def Pascals1(n,r):
    
    res = 1
    
    for i in range(r):
        res = res * (n-i) 
        res = res // (i+1)
    return res

print(Pascals1(3,1))    


# Type 2 :

def Pascals2(n):
    
    for i in range(1,n+1):
        print(Pascals1(n-1,i-1),end=' ')
    print()

print(Pascals2(3))  


# TYpe 3 :

def generateRow(row):
    ans = 1
    ansRow = [1] #inserting the 1st element
    
    #calculate the rest of the elements:
    for col in range(1, row):
        ans *= (row - col)
        ans //= col
        ansRow.append(ans)
    return ansRow

def pascalTriangle(n):
    ans = []
    
    #store the entire pascal's triangle:
    for row in range(1, n+1):
        ans.append(generateRow(row))
    return ans

if __name__ == '__main__':
    n = 5
    ans = pascalTriangle(n)
    for it in ans:
        for ele in it:
            print(ele, end=" ")
        print()
