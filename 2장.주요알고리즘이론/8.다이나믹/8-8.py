n, m = map(int, input().split())

money = []
for _ in range(n):
    money.append(int(input()))

money.sort()

d = [10001]*(m+1)
d[0]=0

for k in money:
    for i in range(money[0],m+1):
        d[i] = min(d[i], d[i-k]+1)

if(d[m] == 10001):
    print(-1)
else:
    print(d[m])