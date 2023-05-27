def coinChange(coins, amount):
    # Initialize the dynamic programming table with a default value of infinity
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Iterate through each coin denomination
    for coin in coins:
        # Update the dp table for each value from the coin denomination to the desired amount
        for i in range(coin, amount + 1):
            # Choose the minimum between using the coin and not using the coin
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the minimum number of coins required for the desired amount
    return dp[amount]
