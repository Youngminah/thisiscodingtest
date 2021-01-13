N, M = map(int, input().split())

result = 0
for i in range(N):
    data = list(map(int, input().split()))
    mini = min(data)

    result = max(result, mini)

print(result)