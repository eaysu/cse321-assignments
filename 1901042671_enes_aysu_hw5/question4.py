def max_discount(discounts):
    n = len(discounts)

    if n == 0:
        return 0
    if n == 1:
        return discounts[0]

    # initialize dp list
    dp = [0] * n

    dp[0] = discounts[0]
    dp[1] = max(discounts[0], discounts[1])

    # dynamic programming part
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + discounts[i])

    # maximum achievable discount for the entire sequence
    return dp[n - 1]

# test usage
discounts = [10, 5, 15, 20, 10, 25]
result = max_discount(discounts)
print(f"The maximum achievable discount is: {result}")
