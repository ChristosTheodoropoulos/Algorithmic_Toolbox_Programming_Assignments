# Uses python3
import sys

# I noticed that the sequence of the last digit of fibonacci numbers
# is periodic with period 60.
# [0, 1, 1, 2, 3, 5, 8, 3, 1, 4,
#  5, 9, 4, 3, 7, 0, 7, 7, 4, 1,
#  5, 6, 1, 7, 8, 5, 3, 8, 1, 9,
#  0, 9, 9, 8, 7, 5, 2, 7, 9, 6,
#  5, 1, 6, 7, 3, 0, 3, 3, 6, 9,
#  5, 4, 9, 3, 2, 5, 7, 2, 9, 1,
#  0, 1, 1, 2, 3, 5, 8, 3, 1, 4,
#  5, 9, 4, 3, 7, 0, 7, 7, 4, 1,
#  5, 6, 1, 7, 8, 5, 3, 8, 1, 9,
#  0, 9, 9, 8, 7, 5, 2, 7, 9, 6,
#  5, 1, 6, 7, 3, 0, 3, 3, 6, 9,
#  5, 4, 9, 3, 2, 5, 7, 2, 9, 1]
# So i calculated all possible summaries and i holded only the last digit
# of them. Finally the list which was produced, is:
# [0, 1, 1, 2, 4, 7, 2, 0, 3, 4,
#  8, 3, 2, 6, 9, 6, 6, 3, 0, 4,
#  5, 0, 6, 7, 4, 2, 7, 0, 8, 9,
#  8, 8, 7, 6, 4, 1, 6, 8, 5, 4,
#  0, 5, 6, 2, 9, 2, 2, 5, 8, 4,
#  3, 8, 2, 1, 4, 6, 1, 8, 0, 9]

def calculate_summary(m, n):
    # Initialization
    sum_last_digit = []
    sum_last_digit.append(0)
    sum_last_digit.append(1)
    last_digit_fibonacci_number = []
    last_digit_fibonacci_number.append(0)
    last_digit_fibonacci_number.append(1)
    sum1 = 0
    # Calculate the last_digit sequence.
    for i in range(2,60):
        last_digit_fibonacci_number.append((last_digit_fibonacci_number[i-2]+last_digit_fibonacci_number[i-1])%10)
    # Calculate the wanted summary.
    for j in range(m%60,n%60+1):
        sum1 = (sum1 + last_digit_fibonacci_number[j])%10

    return sum1

if __name__ == '__main__':
    # Read the input.
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    # Call the function.
    foo2 = calculate_summary(from_, to)
    # Print the result.
    print(foo2)
