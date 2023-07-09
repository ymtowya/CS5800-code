#!/usr/bin/env python

def find_max_d(arr):
    n = len(arr)

    # dp1[i] denotes the smallest element among arr[0 ... i]
    dp1 = [arr[0]] * n
    for i in range(1, n):
        dp1[i] = min(dp1[i - 1], arr[i])

    # dp2[j] denotes the largest element among arr[j ... n - 1]
    dp2 = [arr[n - 1]] * n
    for j in range(n - 2, -1, -1):
        dp2[j] = max(dp2[j + 1], arr[j])

    # max_D denotes the largest difference so far
    max_D = dp2[0] - dp1[0]
    for k in range(1, n):
        max_D = max(max_D, dp2[k] - dp1[k])
    return max_D

if __name__ == '__main__':
    my_arr = [7, 9, 5, 6, 3, 2]
    print("The max difference of the input array ", my_arr, " is: ")
    print(find_max_d(my_arr))