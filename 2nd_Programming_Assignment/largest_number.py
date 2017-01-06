#Uses python3

import sys

def largest_number(a):
    # The logic for sorting a list with the right way is:
    # Work with strings in the first place,
    # concatenate a and b to first and b and a to last,
    # then compare first and last: when last > first
    # you make the swap, otherwise you continue.
    foo = ""
    bar = ""
    for i in range(len(a)):
        for j in range(len(a)-1):
            foo = a[j] + a[j+1]
            bar = a[j+1] + a[j]
            if (bar > foo):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    res = ""
    for x in a:
        res += x
    return res

if __name__ == '__main__':
    # Take the input.
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
