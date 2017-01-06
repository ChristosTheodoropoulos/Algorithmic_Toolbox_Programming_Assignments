# Uses python3
import sys

def get_majority_element(a, left, right):
    if (left == right):
        return -1
    if (left + 1 == right):
        return a[left]

    median = (left + right - 1)//2
    # Recursive calls.
    left_m = get_majority_element(a, left, median + 1)
    right_m = get_majority_element(a, median + 1, right)

    # Find the majority element in the left part
    # of the array. If that element exists.
    left_count = 0
    for i in range(left, right):
        if a[i] == left_m:
            left_count += 1
    if left_count > (right-left)//2:
        return left_m

    # Find the majority element in the right part 
    # of the array. If that element exists.
    right_count = 0
    for i in range(left, right):
        if a[i] == right_m:
            right_count += 1
    if right_count > (right-left)//2:
        return right_m

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
