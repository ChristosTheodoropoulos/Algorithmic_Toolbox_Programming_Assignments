# Uses python3
import sys

# The algorithm maintains in its local variables a sequence element
# and a counter, with the counter initially zero. It then processes
# the elements of the sequence, one at a time.
# When processing an element x, if the counter is zero,
# the algorithm stores x as its remembered sequence element
# and sets the counter to one.
# Otherwise, it compares x to the stored element and either increments
# the counter (if they are equal) or decrements the counter (otherwise).
# At the end of this process, if the sequence has a majority,
# it will be the element stored by the algorithm.
# ----------------------------------------------------------------------
# Even when the input sequence has no majority, the algorithm will report
# one of the sequence elements as its result.
# However, it is possible to perform a second pass over the same input
# sequence in order to count the number of times the reported element
# occurs and determine whether it is actually a majority.
# This second pass is needed, as it is not possible for
# a sublinear-space algorithm to determine whether there exists a
# majority element in a single pass through the input

def boyer_moore_majority_vote (a):
    counter = 0
    m = -1
    for x in a:
        if (counter == 0):
            m = x
            counter = 1
        elif (m == x):
            counter += 1
        else:
            counter -= 1

    return m

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    possible_majority_element = boyer_moore_majority_vote (a)
    counter = 0
    for x in a:
        if (possible_majority_element == x):
            counter += 1
    if (counter > n//2):
        print (1)
    else:
        print (0)
