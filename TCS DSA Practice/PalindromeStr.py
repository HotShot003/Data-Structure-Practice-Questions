# # Problem: Given a string, check if it’s a palindrome (reads the same forward and backward, ignoring case and non-alphanumeric characters).

# def is_palindrome(s):
#     # Convert to lowercase and filter alphanumeric characters
#     s = ''.join(char.lower() for char in s if char.isalnum())
#     # Use two pointers to check palindrome
#     left, right = 0, len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# # Input handling
# s = input()
# print(is_palindrome(s))

def is_palindrome(s):
    # Step 1: Initialize an empty list to store cleaned characters
    cleaned_chars = []
    
    # Step 2: Loop through each character in the input string
    for char in s:
        # Keep only letters and numbers (ignore punctuation & spaces)
        if char.isalnum():
            # Convert to lowercase and add to the list
            cleaned_chars.append(char.lower())
    
    # Step 3: Join the cleaned characters into a single string
    cleaned_str = ''.join(cleaned_chars)
    
    # Step 4: Get the reversed version of the string
    reversed_str = cleaned_str[::-1]
    # print(reversed_str)
    
    # Step 5: Check if original and reversed strings are the same
    if cleaned_str == reversed_str:
        return True
    else:
        return False

# Input handling
user_input = input("Enter a string: ")
print(is_palindrome(user_input))