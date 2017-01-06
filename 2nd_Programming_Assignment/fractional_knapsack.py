# Uses python3
import sys

def get_optimal_value(n, capacity, weights, values):
    # Initializations
    value = 0.
    max_value = -1
    max_index = -1
    for i in range(0, n):
        if (capacity == 0):     # If there is no empty space return value.
            return value
        # Find the item with the maximal value per unit of weight.
        for j in range(0, n):
            if ((weights[j] > 0) and values[j]/weights[j] >= max_value):
                max_value = values[j]/weights[j]
                max_index = j
        # Put the greatest possible quantity of the chosen item in the bag.
        if (capacity >= weights[max_index]):
            value += values[max_index]
            capacity -= weights[max_index]
            weights[max_index] = 0
        else:
            value += capacity*(values[max_index]/weights[max_index])
            capacity = 0
        # Initialize again the variables for the next iteration.
        max_value = -1
        max_index = -1
    return value


if __name__ == "__main__":
    # Read the Input.
    data = list(map(int, sys.stdin.read().split()))
    # Set up the input variables.
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(n, capacity, weights, values)
    print("{:.10f}".format(opt_value))
