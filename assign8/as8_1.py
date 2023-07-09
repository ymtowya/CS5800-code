#!/usr/bin/env python

def find_max_d(arr):
    n = len(arr)
    if n == 1:
        return 0
    
    min_v = arr[0]
    max_D = 0

    for i in range(1, n):
        # update the minimum value so far
        min_v = min(arr[i], min_v)
        # update the maximum difference so far
        max_D = max(arr[i] - min_v, max_D)

    return max_D

if __name__ == '__main__':
    my_arr = [2, 3, 10, 6, 4, 8, 1]
    print("The max difference of the input array ", my_arr, " is: ")
    print(find_max_d(my_arr))