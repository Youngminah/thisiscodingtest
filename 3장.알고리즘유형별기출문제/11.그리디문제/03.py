str = input()
n = len(str)

total = 1
for i in range(1,n):
    if str[i] != str[i-1]:
        total += 1

print( total//2 )