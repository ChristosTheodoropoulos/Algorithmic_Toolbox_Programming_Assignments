#Uses python3

import sys

# Function which implements sorting (mergesort)
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
        return alist

def max_dot_product(a, b):
    # In the beginning sort the two lists
    if (len(a) > 1):
        a = mergeSort(a)
    if (len(b) > 1):
        b = mergeSort(b)
    # Initialize the result and then calculate the
    # final result.
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    # Read input.
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # Set up right the input variables.
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
