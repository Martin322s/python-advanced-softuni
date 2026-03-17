def choose_coins(coins, target_sum):
    coins.sort(reverse=True)
    used_coins = {}
    index = 0

    while target_sum > 0 and index < len(coins):
        coin = coins[index]
        count = target_sum // coin

        if count > 0:
            used_coins[coin] = count
            target_sum -= coin * count

        index += 1

    if target_sum != 0:
        return "Error"

    total_coins = sum(used_coins.values())
    result = [f"Number of coins to take: {total_coins}"]

    for coin, count in used_coins.items():
        result.append(f"{count} coin(s) with value {coin}")

    return '\n'.join(result)


coins = list(map(int, input().split(', ')))
target = int(input())
print(choose_coins(coins, target))