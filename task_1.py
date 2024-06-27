import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    change = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            change[coin] = count
            amount -= coin * count
    return change

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [0] + [float('inf')] * amount
    coin_count = [{}] + [{} for _ in range(amount)]
    
    for coin in coins:
        for x in range(coin, amount + 1):
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                coin_count[x] = coin_count[x - coin].copy()
                if coin in coin_count[x]:
                    coin_count[x][coin] += 1
                else:
                    coin_count[x][coin] = 1
    
    return coin_count[amount]

def compare_algorithms():
    test_amounts = [113, 1000, 10000, 100000]
    greedy_times = []
    dp_times = []
    
    for amount in test_amounts:
        start_time = time.time()
        find_coins_greedy(amount)
        greedy_times.append(time.time() - start_time)
        
        start_time = time.time()
        find_min_coins(amount)
        dp_times.append(time.time() - start_time)
    
    return greedy_times, dp_times

# Example usage:
if __name__ == "__main__":
    # Test the functions
    print("Greedy algorithm result for 113:", find_coins_greedy(113))
    print("Dynamic programming result for 113:", find_min_coins(113))
    
    # Compare performance
    greedy_times, dp_times = compare_algorithms()
    print("Greedy times:", greedy_times)
    print("DP times:", dp_times)
