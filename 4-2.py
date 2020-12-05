n = int(input())


result = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if k % 10 == n or k // 10 == n:
                result += 1
            elif j % 10 == n or j // 10 == n:
                result += 1
            elif i % 10 == n or i // 10 == n:
                result += 1

print(result)