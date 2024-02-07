import time

def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result


def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

start_time = time.time()
find_coins_greedy(12345678)
greedy_time = time.time() - start_time
print(f"Жадібний алгоритм: {find_coins_greedy(12345678)} виконався за {greedy_time} секунд")

start_time = time.time()
find_min_coins(12345678)
dp_time = time.time() - start_time
print(f"Алгоритм динамічного програмування: {find_min_coins(12345678)} виконався за {dp_time} секунд")
