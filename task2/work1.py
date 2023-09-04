 # Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
 # а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
 # чтобы все монетки были повернуты вверх одной и той же стороной.
 # Выведите минимальное количество монет, которые нужно перевернуть


def min_flips_to_same_side(coins):
    if not coins:
        return 0

    flips = 0
    current_side = coins[0]

    for coin in coins:
        if coin != current_side:
            flips += 1
            current_side = coin

    return flips

# Пример использования
n = int(input("Введите количество монеток: "))
coins = []
for i in range(n):
    coin = input(f"Введите сторону монетки {i+1} (решка - R, герб - G): ")
    coins.append(coin)

min_flips = min_flips_to_same_side(coins)
print(f"Минимальное количество переворотов: {min_flips}")
