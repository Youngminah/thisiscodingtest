
str = input()

n = len(str)
a = []
total = 0

for i in range(n):
    a.append(int(str[i]))


for i in range(n):
    c = a[i]
    if i == n-1:
        break
    if i == 0 and (c == 0 or c == 1 or a[i+1] == 0 or a[i+1] == 1):
        total = c + a[i+1]
    elif i == 0 :
        total = c * a[i+1]
    elif c == 0 or c == 1  or a[i+1] == 0 or a[i+1] == 1:
        total = total + a[i+1]
    else:
        total = total * a[i+1]


print(total)

