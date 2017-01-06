# Uses python3
import sys

def binary_search(a, x, left, right):
    # Find the median of the part of the array
    # which i want to check.
    median = (left + right)//2
    # Check if you find the element.
    # If you find it return the index of the array (median).
    # If you don't call again the function binary_search
    # with the part of the array where it's possible the
    # element to be. In addition check if the element finally
    # doesn't be in the array (if (right - left == 1)).
    # In this case return -1.
    if (x == a[median]):
        return median
    elif (x > a[median]):
        if (right - left == 1):
            return -1
        else:
            return binary_search(a, x, median, right)
    elif (x < a[median]):
        if (right - left == 1):
            return -1
        else:
            return binary_search(a, x, left, median)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x, 0, len(a)), end = ' ')
