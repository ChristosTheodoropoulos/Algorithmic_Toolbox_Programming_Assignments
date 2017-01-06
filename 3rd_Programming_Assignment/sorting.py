#Uses python3

# Import libraries.
import sys
import random
R = random.Random(42)

# Function which call quicksort.
def qsort(L):
	quicksort(L,0,len(L))

def quicksort(L,start,stop):
	if stop - start < 2:
        return
    # Random pick a pivot.
	key = L[R.randrange(start,stop)]
    # Initializations.
	m1 = u = start
	m2 = stop
    # Make the partitions.
	while u < m2:
		if L[u] < key:
			swap(L,u,m1)
			m1 += 1
			u = u + 1
		elif L[u] == key:
			u = u + 1
		else:
			m2 = m2 - 1
			swap(L,u,m2)
    # Recursively call quicksort until the work is done.
	quicksort(L, start, m1)
	quicksort(L, m2 ,stop)

# Function for swapping.
def swap(A,i,j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp


if __name__ == '__main__':
    # Read input.
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # Call qsort function.
    qsort(a)
    # Print the final result.
    for x in a:
        print(x, end=' ')
