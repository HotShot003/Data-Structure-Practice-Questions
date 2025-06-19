# Remove all occurrences of a specific value from an array in-place.



def remove_in_place(arr, val):
    write = 0
    for read in range(len(arr)):
        if arr[read] != val:
            arr[write] = arr[read]
            write += 1
    # Optionally, truncate the array to the new length
    del arr[write:]
    return arr

# Example usage:
arr = list(map(int,input().split()))
rem = int(input('Removing Occurance Element : '))
remove_in_place(arr, rem)
print(arr)  # Output: [1, 3, 4, 5]