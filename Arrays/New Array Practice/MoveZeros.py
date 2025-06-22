# Move all zeros to the end of an array while maintaining the relative order of non-zero elements.

def moveZeroes(nums):
    j = 0  # Pointer for the next non-zero element
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums

nums = list(map(int,input().split()))

print(moveZeroes(nums))