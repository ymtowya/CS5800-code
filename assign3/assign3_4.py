#!/usr/bin/env python
# How to run this:
# 1. Put in the numbers with the form as in ./example_input.txt
# 2. Run command: python3 assign3_4.py
# 3. Check the output

# input array
my_arr = []

# read the values of array from the file
def set_arr(line):
    read_ins = []
    numbers_str = line[1:-2]
    numbers = numbers_str.split(",")
    for num in numbers:
        read_ins.append(int(num))
    return read_ins

# calculate the maximum product of subarray of the input array
def get_max_product(nums):
    n = len(nums) # get length of input array
    pos_max = [1] * (n + 1) # an array tracking the so-far maximum positive product
    neg_min = [1] * (n + 1) # an array tracking the so-far minimum negative product
    max_val = nums[0] # store the result
    for i in range(0, n):
        if (nums[i] >= 0):
            # current value is non-negative, update the 2 tracking arrays
            pos_max[i + 1] = max(nums[i], pos_max[i] * nums[i])
            neg_min[i + 1] = min(nums[i], neg_min[i] * nums[i])
        else:
            # current value is negative, update the max & min in reversed order
            pos_max[i + 1] = max(nums[i], neg_min[i] * nums[i])
            neg_min[i + 1] = min(nums[i], pos_max[i] * nums[i])
        if pos_max[i + 1] > max_val:
            # keep updating the so-far maximum product result
            max_val = pos_max[i + 1]
    return max_val

if __name__ == '__main__':
    with open("example_input.txt", "r") as file:
        line = file.readline()
        while not (line is None) and line != "":
            if line[0] == '[':
                # read numbers from file
                my_arr = set_arr(line)
                # print out results
                print("The max product of subarray of the input array ", my_arr, " is:")
                print(get_max_product(my_arr))
            line = file.readline()