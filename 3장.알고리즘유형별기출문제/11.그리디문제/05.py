n, m  = map(int, input().split())
bowl = list(map(int, input().split()))

total =0
for i in range(n):
    for j in range(i, n):
        if bowl[i] != bowl[j]:
            total += 1

print(total)
