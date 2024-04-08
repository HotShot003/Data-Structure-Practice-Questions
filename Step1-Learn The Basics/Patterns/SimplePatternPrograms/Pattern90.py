# Sol 1: Brute force

# def pattern(n):
#     fibonacci_sequence = [1, 1, 2, 3, 5, 8, 13, 21,34,55,89,144,233,377,670]  # Predefined Fibonacci sequence
#     index = 0
#     for i in range(1, n + 2):
#         for j in range(1, n + 2):
#             if i - j >= 0:
#                 # Print Fibonacci number instead of '*'
#                 print(fibonacci_sequence[index], end=' ')
#                 index = (index + 1) % len(fibonacci_sequence)  # Move to next Fibonacci number cyclically
#         print()

# pattern(4)

# # 1 
# # 1 2
# # 3 5 8
# # 13 21 34 55
# # 89 144 233 377 670



# SOl 2 :::

def fibonacci(n):
    fib_sequence = [1, 1]  # Initialize Fibonacci sequence with the first two numbers
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Append next Fibonacci number
    return fib_sequence

def pattern(n):
    fib_seq = fibonacci(n * n)  # Generate enough Fibonacci numbers to fill the pattern
    index = 0
    for i in range(1, n + 2):
        for j in range(1, n + 2):
            if i - j >= 0:
                # Print Fibonacci number instead of '*'
                print(fib_seq[index], end=' ')
                index += 1
        print()

pattern(4)

# 1 
# 1 2
# 3 5 8
# 13 21 34 55
# 89 144 233 377 610
