# 6. Power-logarithmic
# 1. You are given a number x.
# 2. You are given another number n.
# 3. You are required to calculate x raised to the power n.
# Examples:
# Input : 2 5
# Output : 32

def power_logarithmic(n, r):
    if r == 0:
        return 1
    elif r % 2 == 0:
        return power_logarithmic(n*n, r//2)
    else:
        return n * power_logarithmic(n*n, (r-1)//2)

print(power_logarithmic(4,2))

# print(2//2)