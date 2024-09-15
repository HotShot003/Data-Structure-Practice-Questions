T = int(input().strip())

# Process each test case
for _ in range(T):
    N = int(input().strip())
    max_height = 0
    

    for _ in range(N):
        height = int(input().strip())
        if height > max_height:
            max_height = height
            
    print(max_height)
