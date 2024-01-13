def solution(A):
    N = len(A)

    # Edge case: if there are fewer than 2 days, no profit is possible
    if N < 2:
        return 0

    # Initialize variables to keep track of the minimum price and maximum profit
    min_price = A[0]
    max_profit = 0

    # Iterate through the array to find the maximum profit
    for price in A[1:]:
        # Update the minimum price if a lower price is encountered
        min_price = min(min_price, price)

        # Calculate the profit if selling at the current price
        current_profit = price - min_price

        # Update the maximum profit if a higher profit is encountered
        max_profit = max(max_profit, current_profit)

    return max_profit


# Example usage:
stock_prices = [23171, 21011, 21123, 21366, 21013, 21367]
result = solution(stock_prices)
print("Maximum Possible Profit:", result)
