#!/usr/bin/python3
"""Making Change Problem"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize a list to store the minimum coins needed for each value from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Iterate through all possible values from 1 to total
    for value in range(1, total + 1):
        # Try all coin denominations to find the minimum
        for coin in coins:
            if value >= coin:
                dp[value] = min(dp[value], dp[value - coin] + 1)
    
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]

# Test cases
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1

