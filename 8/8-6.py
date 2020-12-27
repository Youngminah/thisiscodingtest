n = int(input())

a = list(map(int, input().split()))

d = [0]*(n+1)

for i in range(n):
    if i == 0:
        d[i] = a[i]
    elif i ==1:
        d[i] = max(a[i-1],a[i])
    else:
        d[i] = max(d[i-1],d[i-2]+a[i])

print(d[n-1])