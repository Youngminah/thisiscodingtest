n = int(input())

list =[]
for _ in range(n):
    list.append(int(input()))

list.sort(reverse=True)

print(list)