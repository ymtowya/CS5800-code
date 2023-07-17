#!/usr/bin/env python

def longestCommonSubsequence(text1: str, text2: str) -> int:
    m = len(text1) 
    n = len(text2)
    dp1 = [0 for i in range(n + 1)]
    dp2 = [0 for i in range(n + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp1[j] = dp2[j - 1] + 1
            else:
                dp1[j] = max(dp1[j-1], dp2[j])
        dp3 = dp2.copy()
        dp2 = dp1
        dp1 = dp3
    
    return dp2[n]

if __name__ == '__main__':
    x = "abcde"
    y = "ace"
    print("The longest common subsequence length of the input strings is: ")
    print(longestCommonSubsequence(x, y))