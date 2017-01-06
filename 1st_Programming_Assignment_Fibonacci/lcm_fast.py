# Uses python3
import sys

# Function which calculated the GCD
def gcd(a, b):
    if b == 0:
        return a
    temp = a % b
    return gcd(b,temp)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # Use the property: LCM(a,b)*GCD(a,b) = a*b
    # in order to calculate efficiently the lcm.
    gcd = gcd(a, b)
    mult = a * b
    lcm = mult//gcd   # //:Return integer as result not float
    print(lcm)
