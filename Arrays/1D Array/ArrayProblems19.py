# Stocks Buy and Sell ::

# Sol 1: Optimal
def maxProfit(arr):
    maxPro = 0
    minPrice = float('inf')
    for i in range(len(arr)):
        minPrice = min(minPrice, arr[i])
        maxPro = max(maxPro, arr[i] - minPrice)
    return maxPro

arr = [7, 1, 5, 3, 6, 4]
maxPro = maxProfit(arr)
print("Max profit is:", maxPro)

#Sol 2:

def maxProfit1(arr):
    buy = arr[0]
    profit = 0
    
    for i in range(len(arr)):
        
        if arr[i] < buy:
            buy = arr[i]
        
        elif arr[i] - buy > profit:
            profit = arr[i] - buy
    
    return profit     
print(maxProfit1(arr))       