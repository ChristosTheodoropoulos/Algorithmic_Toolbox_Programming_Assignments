# Uses python3

# Read input
n = int(input())
# Initialization
last_digit_fibonacci_number = []
last_digit_fibonacci_number.append(0)
last_digit_fibonacci_number.append(1)
# Calculate the fibonacci numbers and store the in the list.
for i in range(2,n+1):
    last_digit_fibonacci_number.append((last_digit_fibonacci_number[i-2]+last_digit_fibonacci_number[i-1]) % 10)

# Print fn
print(last_digit_fibonacci_number[n])
