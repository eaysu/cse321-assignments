def exhaustive_search(coins, target_amount, current_amount=0, current_count=0, remaining_coins=None):
    if remaining_coins is None:
        remaining_coins = coins

    if current_amount == target_amount:
        return current_count
    elif current_amount > target_amount or not remaining_coins:
        return float('inf')

    use_current_coin = exhaustive_search(
        coins,
        target_amount,
        current_amount + remaining_coins[0],
        current_count + 1,
        remaining_coins
    )
    skip_current_coin = exhaustive_search(
        coins,
        target_amount,
        current_amount,
        current_count,
        remaining_coins[1:]
    )

    return min(use_current_coin, skip_current_coin)

# Example usage
coins = [1, 5, 10, 25]
target_amount = 63
result = exhaustive_search(coins, target_amount)
print(f"Minimum number of coins to make {target_amount} cents: {result}")
