coins = int(input()), int(input()), int(input())
target  = int(input())

# 総当りで解いてみる
count = 0
for coin500 in range(coins[0]+1):
    for coin100 in range(coins[1]+1):
        for coin50 in range(coins[2]+1):
            value = 500 * coin500 + 100 * coin100 + 50 * coin50
            if value == target:
                count += 1

print(count)
