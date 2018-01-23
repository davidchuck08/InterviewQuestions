#!/usr/bin/python
'''
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1
'''
import sys
def coinChange(coins, amount):
    if coins is None or len(coins)==0:
        return -1
    dp = [sys.maxint for i in range(amount+1)]
    dp[0]=0
    for i in range(amount+1):
        for coin in coins:
            if i < coin:
                continue
            dp[i]=min(dp[i], dp[i-coin]+1)
    if dp[-1]>=sys.maxint:
        return -1
    return dp[-1]
           
            







'''
import sys
def coinChange(coins, amount):
    if coins is None or len(coins) ==0:
        print 'coin set is None'
        return -1
    dp = [sys.maxint for i in range(amount+1)]
    dp[0]=0
    for i in range(amount+1):
        for coin in coins:
            print i, coin
            if i < coin:
                continue
            dp[i]=min(dp[i], dp[i-coin]+1)
    print dp
    if dp[-1]>=sys.maxint:
        return -1
    print dp
    return dp[-1]
'''
coins = [1,2,5]
amount=3

print coinChange(coins, amount)