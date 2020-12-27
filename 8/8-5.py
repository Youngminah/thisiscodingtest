n = int(input())

d = [0]*(n+1)

for i in range(2,n+1):
    tmp = d[i-1]+1

    if i%2 == 0:
        tmp = min(tmp, d[i//2] + 1)
    if i%3 == 0:
        tmp = min(tmp, d[i//3] + 1)
    if i%5 == 0:
        tmp = min(tmp, d[i//5] + 1)

    d[i] = tmp


print(d[n])