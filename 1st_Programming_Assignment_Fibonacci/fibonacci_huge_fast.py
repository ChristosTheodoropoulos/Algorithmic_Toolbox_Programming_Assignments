# Uses python3
import sys

def calculate_fibonacci_number_modulo_m(n, m):
    # Initialization
    fibonacci_number_modulo_m = []
    fibonacci_number_modulo_m.append(0)
    fibonacci_number_modulo_m.append(1)
    foo1 = False
    for i in range(2,n+1):
        fibonacci_number_modulo_m.append((fibonacci_number_modulo_m[i-2]+fibonacci_number_modulo_m[i-1])%m)
        # This if-statement checks if we are at the end of the period
        # in order to find the length of the period.
        if ((fibonacci_number_modulo_m[i-1] == 0) and (fibonacci_number_modulo_m[i] == 1)):
            foo1 = True
            length = i - 1
            break
    if foo1 == False:
        return fibonacci_number_modulo_m[n]
    else:
        temp = n % length
        return fibonacci_number_modulo_m[temp]


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(calculate_fibonacci_number_modulo_m(n,m))
