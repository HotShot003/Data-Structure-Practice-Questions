# Basic Recurtion Print Name

def names(s):
    
    if s == 0:
        return
    
    # print(f"Anurag {s-1}") # PRint in descending order
    names(s-1)
    print(f"Anurag {s-1}")  # Print in ascending order


names(5)