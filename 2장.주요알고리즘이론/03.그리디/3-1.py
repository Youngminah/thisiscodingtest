N = 1260

coins = [500, 100, 50, 10]

result =0
for i in coins:
	result += N // i
	N = N % i

print(result)