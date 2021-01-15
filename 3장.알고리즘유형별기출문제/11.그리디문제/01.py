n = int(input())

people = list(map(int, input().split()))

people.sort()

count = 0
index = 0
for i in range(n-1,-1,-1):
    m = people[i]
    index += m

    if index-1 >= i and index <= n:
        count += 1
        break
    elif index-1 >= i and index > n:
        break
    else :
        count += 1

print(count)