#!/usr/bin/env python

def lengthOfLIS(nums) -> int:
    n = len(nums)
    dp = [1 for i in range(n + 1)]
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)

if __name__ == '__main__':
    x = [10,9,2,5,3,7,101,18]
    print("The length of longest increasing subsequence of the input array is: ")
    print(lengthOfLIS(x))