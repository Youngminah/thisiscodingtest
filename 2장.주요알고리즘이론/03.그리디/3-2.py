N, M, K = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[N - 1]
second = data[N - 2]

result = 0

for i in range(M):
    if (i + 1) % 3 == 0:
        result += second
    else:
        result += first

print(result)