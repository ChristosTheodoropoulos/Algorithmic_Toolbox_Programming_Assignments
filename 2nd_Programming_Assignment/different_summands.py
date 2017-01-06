# Uses python3
import sys

def optimal_summands(n):
    # Initializations.
    remainder = n   # Available candies.
    summands = []
    for i in range(1, n+1):
        # Check if you can create two different sets.
        # If you can create the one of them and continue.
        # If you can't create one set with all the
        # available candies and stop.
        if (i + (i+1)) <= remainder:
            summands.append(i)
            remainder = remainder - i
        else:
            summands.append(remainder)
            remainder = 0
        if (remainder == 0):
            break
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
