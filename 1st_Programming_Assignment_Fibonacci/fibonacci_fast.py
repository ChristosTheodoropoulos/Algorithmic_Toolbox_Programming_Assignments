# Uses python3

# Read input
n = int(input())
# Initialization
fibonacci_number = []
fibonacci_number.append(0)
fibonacci_number.append(1)
# Calculate the fibonacci numbers and store the in the list.
for i in range(2,n+1):
    fibonacci_number.append(fibonacci_number[i-2]+fibonacci_number[i-1])

# Print fn
print(fibonacci_number[n])
