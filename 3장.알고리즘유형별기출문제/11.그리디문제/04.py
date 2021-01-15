n = int(input())
coins = list(map(int, input().split()))

coins.sort()

coin = 1
for c in coins:
    if coin < c:
        break
    coin += c

print(coin)


