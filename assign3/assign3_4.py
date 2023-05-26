#!/usr/bin/env python

# input array
my_arr = [2, 3, -2, 4]

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
    print("The max product of subarray of the input array ", my_arr, " is:")
    print(get_max_product(my_arr))