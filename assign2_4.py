
my_array = []
my_thres = 0
# my_expected = 0

# Set the array of numbers by the reading input
def set_arr(line):
    my_array = []
    numbers_str = line[1:-2]
    numbers = numbers_str.split(", ")
    for num in numbers:
        my_array.append(int(num))
    return my_array

# Set the threshold
def set_thres(line):
    my_thres = float(line)
    return my_thres
    
def set_expected(line):
    my_expected = int(line)
    return my_expected

# Get the critical number
def find_critical_number(arr, threshold):
    count = 0
    n = len(arr)
    for index, item in enumerate(arr):
        for j in range(index + 1, n, 1):
            if (item > threshold * arr[j]):
                count += 1
    return count

# Do the computation and print out the result
def do_compute_then_compare(my_array, my_thres):
    res = find_critical_number(my_array, my_thres)
    print("The array is: ", my_array)
    print("The threshold is: ", my_thres)
    print("The actual result is: ", res)
    print("\n")

with open("example_input.txt", "r") as file:
    line = file.readline()
    while not (line is None) and line != "":
        if line[0] == '[':
            my_array = set_arr(line)
            line = file.readline()
            my_thres = set_thres(line)
            do_compute_then_compare(my_array, my_thres)
        line = file.readline()
