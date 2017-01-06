# Uses python3
import sys

def optimal_points(start, end):
    # Initializations
    points = []
    min_value = 1000000000000000
    flag = False
    for j in range(len(end)):
        # Find the minimum value in end list.
        # Check only the elements with non-zero value.
        for i in range(len(end)):
            if (end[i] < min_value and end[i] != 0):
                min_value = end[i]
                min_index = i
                flag = True
        # If the minimum value has changed, put the point
        # in list points.
        if (flag == True):
            points.append(min_value)
        # Collect all the signatures you can.
        # Set the appropriate elements in end list
        # equal with zero, because your are done with
        # these tenants.
        for i in range(len(start)):
            if (start[i] <= min_value):
                end[i] = 0
        # Initialize again the variables for the next iteration.
        min_value = 1000000000000000
        flag = False
    return points

if __name__ == '__main__':
    # Take the input.
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    # Convert input to proper form.
    start = []
    end = []
    for i in range(len(data)):
        if i % 2 == 0:
            start.append(data[i])
        else:
            end.append(data[i])
    points = optimal_points(start, end)
    print(len(points))
    for p in points:
        print(p, end=' ')
