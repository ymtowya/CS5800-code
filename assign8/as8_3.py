#!/usr/bin/env python

def find_max_sub(arr):
    n = len(arr)

    # helper array dp
    dp = [0] * n

    # dp[i] denotes that if the subarray ends at arr[i], then the maximum sum this 
    # subarray can reach
    dp[0] = arr[0]
    
    for i in range(1, n):
        # to reach the maximum sum of subarray ends at arr[i]
        # it either only contains arr[i], or will add it into the previous subarray arr[ ... i-1 ]
        # update with the larger value
        dp[i] = max(dp[i - 1] + arr[i], arr[i])
    
    # find the maximum sum of subarray among subarrays ends with arr[0] ... arr[n-1]
    return max(dp)

if __name__ == '__main__':
    my_arr = [1, -3, 6, -5, 9, 2, -1, 5, -7, 5]
    print("Input array : ", my_arr)
    print("Result : ", find_max_sub(my_arr))