n = int(input())

arr= []
for _ in range(n):
    name, score = input().split()
    score = int(score)
    arr.append((name, score))


arr = sorted(arr, key = lambda student: student[1])

print(arr)