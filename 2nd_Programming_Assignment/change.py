# Uses python3
import sys

def get_change(m):
    remainder = m   
    m = 0   # Number of coins
    while (remainder != 0):
        if (remainder >= 10):
            m += remainder//10
            remainder = remainder%10
        elif (remainder >= 5):
            m += remainder//5
            remainder = remainder%5
        else:
            m += remainder
            remainder = 0
    return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
