#!/usr/bin/env python

def find_coin_num(coins, S):
    # sort the coins by value
    coins.sort()
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
            # we add add this coin to the solution
            if m >= coin:
                # update the dp with minimum number of coins to reach this value
                dp[m] = min(dp[m - coin] + 1, dp[m])
            else:
                # we don't need to consider larger coins
                break
    
    if dp[S] == INF:
        return -1
    return dp[S]

if __name__ == '__main__':
    S = 13
    my_arr = [1, 3, 5, 7, 9]
    print("Coins array : ", my_arr)
    print("Target value : ", S)
    print(find_coin_num(my_arr, S))

