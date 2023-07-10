#!/usr/bin/env python

def find_coin_num(coins, S):
    n = len(coins)
    INF = 99999999
    # init the dp array with max value
    dp = [INF] * (S + 1)
    # 0 requires 0 coins
    dp[0] = 0

    # start from the small value to our target
    for m in range(1, S + 1):
        # traverse each type of coin
        for i in range(n):
            coin = coins[i]
            # if we can add this coin to the solution
            if m >= coin:
                # update the dp with minimum number of coins to reach this value
                dp[m] = min(dp[m - coin] + 1, dp[m])
    
    if dp[S] == INF:
        return -1
    return dp[S]

if __name__ == '__main__':
    S = 13
    my_arr = [3, 7, 9, 1, 5]
    print("Coins array : ", my_arr)
    print("Target value : ", S)
    print(find_coin_num(my_arr, S))

